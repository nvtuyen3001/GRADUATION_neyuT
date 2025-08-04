from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Define Models
class Friend(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class FriendCreate(BaseModel):
    name: str

class GraduationInfo(BaseModel):
    graduate_name: str = "Nguyen Van Tuyen"
    major: str = "Khoa học máy tính"
    university: str = "Hanoi University of Industry"
    date: str = "19/8/2025"
    time: str = "08:00"
    location: str = "Tầng 3 - Thư viện tòa A11"
    address: str = "Số 298 Đ. Cầu Diễn, Minh Khai, Bắc Từ Liêm, Hà Nội"

# Routes
@api_router.get("/")
async def root():
    return {"message": "Graduation Invitation API"}

@api_router.post("/friends", response_model=Friend)
async def create_friend(input: FriendCreate):
    friend_dict = input.dict()
    friend_obj = Friend(**friend_dict)
    await db.friends.insert_one(friend_obj.dict())
    return friend_obj

@api_router.get("/friends", response_model=List[Friend])
async def get_friends():
    friends = await db.friends.find().to_list(1000)
    return [Friend(**friend) for friend in friends]

@api_router.get("/friends/{friend_id}", response_model=Friend)
async def get_friend(friend_id: str):
    friend = await db.friends.find_one({"id": friend_id})
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    return Friend(**friend)

@api_router.get("/graduation-info")
async def get_graduation_info():
    return GraduationInfo()

@api_router.post("/init-data")
async def init_sample_data():
    # Clear existing data
    await db.friends.delete_many({})
    
    # Add sample friends
    sample_friends = [
        {"name": "Ha Nguyen Tuan Kiet"},
        {"name": "Vu Van Hau"}
    ]
    
    for friend_data in sample_friends:
        friend_obj = Friend(**friend_data)
        await db.friends.insert_one(friend_obj.dict())
    
    return {"message": "Sample data initialized"}

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()