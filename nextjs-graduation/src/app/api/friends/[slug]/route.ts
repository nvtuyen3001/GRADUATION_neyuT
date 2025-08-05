import { NextRequest, NextResponse } from 'next/server';
import clientPromise from '@/lib/mongodb';

// GET /api/friends/[slug] - Get friend by slug
export async function GET(
  req: NextRequest,
  { params }: { params: Promise<{ slug: string }> }
) {
  try {
    const { slug } = await params;
    
    const client = await clientPromise;
    const db = client.db(process.env.DB_NAME || 'graduation_db');
    
    const friend = await db.collection('friends').findOne({ slug });
    
    if (!friend) {
      return NextResponse.json({ error: 'Friend not found' }, { status: 404 });
    }
    
    return NextResponse.json({
      id: friend.id,
      name: friend.name,
      slug: friend.slug,
      created_at: friend.created_at
    });
  } catch (error) {
    console.error('Error fetching friend:', error);
    return NextResponse.json({ error: 'Failed to fetch friend' }, { status: 500 });
  }
}