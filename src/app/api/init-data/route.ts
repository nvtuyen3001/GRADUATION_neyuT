import { NextResponse } from 'next/server';
import clientPromise from '@/lib/mongodb';
import { Friend, createSlug } from '@/lib/models';
import { v4 as uuidv4 } from 'uuid';

// POST /api/init-data - Initialize sample data
export async function POST() {
  try {
    const client = await clientPromise;
    const db = client.db(process.env.DB_NAME || 'graduation_db');
    
    // Clear existing data
    await db.collection('friends').deleteMany({});
    
    // Add sample friends with capitalized names and slugs
    const sampleFriendsData = [
      { name: "HÀ NGUYỄN TUẤN KIỆT" },
      { name: "VŨ VĂN HẬU" },
      { name: "TRẦN THỊ PHƯƠNG LAN" },
      { name: "NGUYỄN THỊ HẠNH" },
      { name: "PHẠM HUYỀN DIỆU" },
      { name: "NGUYỄN THỊ KHUYÊN" },
      { name: "NGUYỄN THỊ PHƯƠNG" },
      { name: "NGUYỄN THỊ HÀ" },
      { name: "PHẠM VĂN ANH TÙNG" },
      { name: "NGUYỄN QUANG THẮNG" },
      { name: "NGUYỄN HỮU TUẤN" }
    ];
    
    const friends: Friend[] = sampleFriendsData.map(friendData => ({
      id: uuidv4(),
      name: friendData.name,
      slug: createSlug(friendData.name),
      created_at: new Date()
    }));
    
    await db.collection('friends').insertMany(friends);
    
    return NextResponse.json({ message: "Sample data initialized" });
  } catch (error) {
    console.error('Error initializing data:', error);
    return NextResponse.json({ error: 'Failed to initialize data' }, { status: 500 });
  }
}