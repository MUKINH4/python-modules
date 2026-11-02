import os
import sys
import dotenv

dotenv.load_dotenv()

def require_venvs() -> list[str]:
    MATRIX_MODE = os.getenv("MATRIX_MODE")
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_KEY = os.getenv("API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")

require_venvs()