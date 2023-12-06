# 방법1
import os
from dotenv import load_dotenv

load_dotenv()

FLASK_APP = os.environ.get('FLASK_APP')
FLASK_ENV = os.getenv("FLASK_ENV")
ACCESSKEY = os.environ.get("ACCESSKEY")
FLASK_ENV = os.getenv("FLASK_ENV")
HOST=os.getenv("HOST")
