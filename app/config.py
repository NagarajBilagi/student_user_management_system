
from dotenv import load_dotenv
import os

load_dotenv()  # Load the .env file

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_IN_ENV")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# API_HOST = os.getenv("API_HOST", "127.0.0.1")
# API_PORT = int(os.getenv("API_PORT", 8000))
