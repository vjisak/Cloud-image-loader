import cloudinary
import os
from dotenv import load_dotenv

load_dotenv()

# Prefer environment variables for secrets. Create a .env file in the project root
# or set these variables in your environment. Example values are in .env.example.
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)