import { NextRequest, NextResponse } from 'next/server';
import clientPromise from '@/lib/mongodb';
import { Friend, FriendCreate, createSlug } from '@/lib/models';
import { v4 as uuidv4 } from 'uuid';

// GET /api/friends - Get all friends
export async function GET() {
  try {
    const client = await clientPromise;
    const db = client.db(process.env.DB_NAME || 'graduation_db');
    
    const friends = await db.collection('friends').find({}).toArray();
    
    return NextResponse.json(friends.map(friend => ({
      id: friend.id,
      name: friend.name,
      slug: friend.slug,
      created_at: friend.created_at
    })));
  } catch (error) {
    console.error('Error fetching friends:', error);
    return NextResponse.json({ error: 'Failed to fetch friends' }, { status: 500 });
  }
}

// POST /api/friends - Create a new friend
export async function POST(req: NextRequest) {
  try {
    const body: FriendCreate = await req.json();
    
    const friend: Friend = {
      id: uuidv4(),
      name: body.name,
      slug: createSlug(body.name),
      created_at: new Date()
    };

    const client = await clientPromise;
    const db = client.db(process.env.DB_NAME || 'graduation_db');
    
    await db.collection('friends').insertOne(friend);
    
    return NextResponse.json(friend);
  } catch (error) {
    console.error('Error creating friend:', error);
    return NextResponse.json({ error: 'Failed to create friend' }, { status: 500 });
  }
}