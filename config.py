import os
from dotenv.main import load_dotenv

load_dotenv()

BAIDU_APP_ID = os.getenv('BAIDU_APP_ID')
BAIDU_APP_SECRET_KEY = os.getenv("BAIDU_APP_SECRET_KEY")


