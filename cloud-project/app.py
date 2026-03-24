from flask import Flask, render_template, request, redirect
import cloudinary.uploader
import config
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

# MongoDB connection (prefer MONGODB_URI from env)
mongo_uri = os.getenv("MONGODB_URI")
if not mongo_uri:
    # fallback to existing hardcoded URI (you should set MONGODB_URI in .env)
    mongo_uri = "mongodb+srv://vjisak555_db_user:Isak2005@cluster0.5hhk6if.mongodb.net/?appName=Cluster0"

client = None
db = None
collection = None
try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # trigger server selection / auth to surface errors early
    client.server_info()
    db = client["cloud_db"]
    collection = db["files"]
except Exception as e:
    print("[ERROR] Could not connect to MongoDB:", e)
    print("Set MONGODB_URI in your environment or check network/auth settings.")

@app.route('/')
def index():
    total_files = collection.count_documents({})
    storage_used = total_files * 2  # approx MB

    return render_template(
        'index.html',
        file_count=total_files,
        storage=storage_used
    )

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    if file:
        result = cloudinary.uploader.upload(file)
        file_url = result['secure_url']

        # Save to MongoDB
        collection.insert_one({
            "url": file_url,
            "filename": file.filename
        })

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    files = list(collection.find())
    return render_template('dashboard.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)