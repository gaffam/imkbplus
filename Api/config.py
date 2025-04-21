import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "data")
START_DATE = os.getenv("START_DATE", "2016-01-01")
