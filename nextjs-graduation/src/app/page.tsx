'use client';

import React, { useEffect, useState } from "react";
import Link from "next/link";
import axios from "axios";
import { Friend } from "@/lib/models";

const HomePage = () => {
  const [friends, setFriends] = useState<Friend[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFriends = async () => {
      try {
        // Initialize sample data first
        await axios.post('/api/init-data');
        
        // Then fetch friends
        const response = await axios.get('/api/friends');
        setFriends(response.data);
      } catch (error) {
        console.error('Error fetching friends:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchFriends();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-200 to-emerald-400">
        <div className="text-2xl font-semibold text-green-800">Đang tải...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-200 to-emerald-400 py-8">
      <div className="container mx-auto px-4">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-green-800 mb-4">
            LỄ TỐT NGHIỆP 2025
          </h1>
          <p className="text-xl text-green-700">
            Nguyen Van Tuyen
          </p>
          <p className="text-lg text-green-600 mt-2">
            Mời các bạn tham dự lễ tốt nghiệp
          </p>
        </div>

        <div className="bg-white/80 backdrop-blur-sm rounded-3xl shadow-2xl p-8 max-w-2xl mx-auto">
          <h2 className="text-3xl font-bold text-center text-green-800 mb-8">
            Danh sách bạn bè
          </h2>
          
          <div className="space-y-4">
            {friends.map((friend) => (
              <Link
                key={friend.id}
                href={`/invite/${friend.slug}`}
                className="block p-6 bg-gradient-to-r from-green-100 to-emerald-100 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105 border-2 border-green-200 hover:border-green-300"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xl font-semibold text-green-800">
                    {friend.name}
                  </span>
                  <span className="text-green-600 font-medium">
                    Nhấn để mở thiệp mời →
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;