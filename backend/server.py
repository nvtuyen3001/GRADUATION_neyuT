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
    slug: str  # URL-friendly version of name
    created_at: datetime = Field(default_factory=datetime.utcnow)

class FriendCreate(BaseModel):
    name: str

def create_slug(name: str) -> str:
    """Convert Vietnamese name to URL-friendly slug"""
    # Convert Vietnamese characters to ASCII
    vietnamese_map = {
        'à': 'a', 'á': 'a', 'ạ': 'a', 'ả': 'a', 'ã': 'a', 'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ậ': 'a', 'ẩ': 'a', 'ẫ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ặ': 'a', 'ẳ': 'a', 'ẵ': 'a',
        'è': 'e', 'é': 'e', 'ẹ': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ê': 'e', 'ề': 'e', 'ế': 'e', 'ệ': 'e', 'ể': 'e', 'ễ': 'e',
        'ì': 'i', 'í': 'i', 'ị': 'i', 'ỉ': 'i', 'ĩ': 'i',
        'ò': 'o', 'ó': 'o', 'ọ': 'o', 'ỏ': 'o', 'õ': 'o', 'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ộ': 'o', 'ổ': 'o', 'ỗ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ợ': 'o', 'ở': 'o', 'ỡ': 'o',
        'ù': 'u', 'ú': 'u', 'ụ': 'u', 'ủ': 'u', 'ũ': 'u', 'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ự': 'u', 'ử': 'u', 'ữ': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỵ': 'y', 'ỷ': 'y', 'ỹ': 'y',
        'đ': 'd',
        'À': 'A', 'Á': 'A', 'Ạ': 'A', 'Ả': 'A', 'Ã': 'A', 'Â': 'A', 'Ầ': 'A', 'Ấ': 'A', 'Ậ': 'A', 'Ẩ': 'A', 'Ẫ': 'A',
        'Ă': 'A', 'Ằ': 'A', 'Ắ': 'A', 'Ặ': 'A', 'Ẳ': 'A', 'Ẵ': 'A',
        'È': 'E', 'É': 'E', 'Ẹ': 'E', 'Ẻ': 'E', 'Ẽ': 'E', 'Ê': 'E', 'Ề': 'E', 'Ế': 'E', 'Ệ': 'E', 'Ể': 'E', 'Ễ': 'E',
        'Ì': 'I', 'Í': 'I', 'Ị': 'I', 'Ỉ': 'I', 'Ĩ': 'I',
        'Ò': 'O', 'Ó': 'O', 'Ọ': 'O', 'Ỏ': 'O', 'Õ': 'O', 'Ô': 'O', 'Ồ': 'O', 'Ố': 'O', 'Ộ': 'O', 'Ổ': 'O', 'Ỗ': 'O',
        'Ơ': 'O', 'Ờ': 'O', 'Ớ': 'O', 'Ợ': 'O', 'Ở': 'O', 'Ỡ': 'O',
        'Ù': 'U', 'Ú': 'U', 'Ụ': 'U', 'Ủ': 'U', 'Ũ': 'U', 'Ư': 'U', 'Ừ': 'U', 'Ứ': 'U', 'Ự': 'U', 'Ử': 'U', 'Ữ': 'U',
        'Ỳ': 'Y', 'Ý': 'Y', 'Ỵ': 'Y', 'Ỷ': 'Y', 'Ỹ': 'Y',
        'Đ': 'D'
    }
    
    # Convert to lowercase and replace Vietnamese characters
    slug = name.lower()
    for viet_char, ascii_char in vietnamese_map.items():
        slug = slug.replace(viet_char, ascii_char)
    
    # Replace spaces with hyphens and remove special characters
    slug = slug.replace(' ', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    
    # Remove multiple consecutive hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')
    
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    
    return slug

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
    friend_dict["slug"] = create_slug(friend_dict["name"])
    friend_obj = Friend(**friend_dict)
    await db.friends.insert_one(friend_obj.dict())
    return friend_obj

@api_router.get("/friends", response_model=List[Friend])
async def get_friends():
    friends = await db.friends.find().to_list(1000)
    return [Friend(**friend) for friend in friends]

@api_router.get("/friends/{friend_slug}", response_model=Friend)
async def get_friend_by_slug(friend_slug: str):
    friend = await db.friends.find_one({"slug": friend_slug})
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
    
    # Add sample friends with capitalized names and slugs
    sample_friends = [
        {"name": "HÀ NGUYỄN TUẤN KIỆT"},
        {"name": "VŨ VĂN HẬU"},
        {"name": "TRẦN THỊ PHƯƠNG LAN"},
        {"name": "NGUYỄN THỊ HẠNH"},
        {"name": "PHẠM HUYỀN DIỆU"},
        {"name": "NGUYỄN THỊ KHUYÊN"},
        {"name": "NGUYỄN THỊ PHƯƠNG"},
        {"name": "NGUYỄN THỊ HÀ"},
        {"name": "PHẠM VĂN ANH TÙNG"},
        {"name": "NGUYỄN QUANG THẮNG"},
        {"name": "NGUYỄN HỮU TUẤN"}
    ]
    
    for friend_data in sample_friends:
        friend_data["slug"] = create_slug(friend_data["name"])
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