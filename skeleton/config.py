import os
from dotenv import load_dotenv

load_dotenv()

# Configuration values
DATA_DIR = os.getenv("DATA_DIR", "data")
RESULTS_DIR = os.getenv("RESULTS_DIR", "results")
START_DATE = os.getenv("START_DATE", "2016-01-01")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
API_USER = os.getenv("API_USER", "admin")
API_PASS = os.getenv("API_PASS", "password")
