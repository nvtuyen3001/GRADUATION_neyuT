import { NextResponse } from 'next/server';
import { GraduationInfo } from '@/lib/models';

// GET /api/graduation-info - Get graduation information
export async function GET() {
  try {
    const graduationInfo: GraduationInfo = {
      graduate_name: "Nguyen Van Tuyen",
      major: "Khoa học máy tính",
      university: "Hanoi University of Industry",
      date: "19/8/2025",
      time: "08:00",
      location: "Tầng 3 - Thư viện tòa A11",
      address: "Số 298 Đ. Cầu Diễn, Minh Khai, Bắc Từ Liêm, Hà Nội",
      university_vietnamese: "Trường Đại Học Công Nghiệp Hà Nội"
    };
    
    return NextResponse.json(graduationInfo);
  } catch (error) {
    console.error('Error fetching graduation info:', error);
    return NextResponse.json({ error: 'Failed to fetch graduation info' }, { status: 500 });
  }
}