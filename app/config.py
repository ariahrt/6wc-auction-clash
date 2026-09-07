import os
from dotenv import load_dotenv

load_dotenv()

OSU_CLIENT_ID = osu.environ["OSU_CLIENT_ID"]
OSU_CLIENT_SECRET = os.environ["OSU_CLIENT_SECRET"]
OSU_REDIRECT_URI = os.environ["OSU_REDIRECT_URI"]
SESSION_SECRET = os.environ["SESSION_SECRET"]
STREAM_TOKEN = os.environ["STREAM_TOKEN"]
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./auction.db")

STARTING_BUDGET = 60
TOTAL_SLOTS = 8