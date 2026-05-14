from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

print(MONGO_URI)

client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)

try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully")
except Exception as e:
    print(e)

db = client["bookstore"]

books_collection = db["books"]