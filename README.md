Cloud-Based File Storage & Management System
A full-stack web application for uploading, storing, and managing files using Cloudinary for media storage, MongoDB Atlas for metadata, and Flask as the backend framework.

Features

Upload any file through a drag-and-drop web interface
Files stored on Cloudinary's global CDN for fast access
File metadata (name + URL) persisted in MongoDB Atlas
Dashboard to view all uploaded files
One-click download directly from Cloudinary's edge network
Secure credential management via environment variables


Tech Stack
LayerTechnologyBackendPython, FlaskCloud StorageCloudinaryDatabaseMongoDB Atlas (PyMongo)FrontendHTML, CSS, Jinja2Configpython-dotenv

Project Structure
cloud-project/
├── app.py               # Flask routes (upload, dashboard, home)
├── config.py            # Cloudinary SDK initialisation
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── templates/
│   ├── index.html       # Upload page
│   └── dashboard.html   # File management dashboard
└── static/
    └── style.css        # Glassmorphism UI styling

Setup & Installation
1. Clone the repository
bashgit clone https://github.com/your-username/cloud-project.git
cd cloud-project
2. Create and activate a virtual environment
bashpython -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Configure environment variables
Copy the example file and fill in your credentials:
bashcp .env.example .env
Then edit .env:
envCLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
MONGODB_URI=mongodb+srv://<user>:<pass>@cluster0.example.mongodb.net/?retryWrites=true&w=majority

Get your Cloudinary credentials at cloudinary.com
Get your MongoDB URI from MongoDB Atlas

5. Run the app
bashpython app.py
Visit http://localhost:5000 in your browser.

Usage

Upload Page (/) — Select a file and click Upload File. The home page also shows your total file count and estimated storage used.
Dashboard (/dashboard) — View all uploaded files. Each file has:

View — Opens the file in a new browser tab via the Cloudinary CDN URL
Download — Downloads the file directly from Cloudinary using the fl_attachment transformation




Environment Variables
VariableDescriptionCLOUDINARY_CLOUD_NAMEYour Cloudinary cloud nameCLOUDINARY_API_KEYYour Cloudinary API keyCLOUDINARY_API_SECRETYour Cloudinary API secretMONGODB_URIMongoDB Atlas connection string

Never commit your .env file. It is already listed in .gitignore.


Dependencies
Flask
pymongo
python-dotenv
cloudinary
Install all with:
bashpip install -r requirements.txt

Future Enhancements

 User authentication and per-user file isolation
 File deletion (Cloudinary destroy API + MongoDB document removal)
 Real file size and upload timestamp display
 File type filtering and search on the dashboard
 Upload progress bar for large files
 Deployment to Render / Railway with HTTPS


License
This project was built for academic purposes as part of the Cloud Essential course at Dr. N.G.P. Institute of Technology, Coimbatore.

Author
Jebamani Isak V— AI & Data Science, Dr. N.G.P. Institute of Technology
