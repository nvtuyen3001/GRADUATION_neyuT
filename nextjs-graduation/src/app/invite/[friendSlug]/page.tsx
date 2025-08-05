'use client';

import React, { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import axios from "axios";
import { Friend } from "@/lib/models";

const InvitationPage = () => {
  const { friendSlug } = useParams();
  const router = useRouter();
  const [friend, setFriend] = useState<Friend | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFriend = async () => {
      try {
        const response = await axios.get(`/api/friends/${friendSlug}`);
        setFriend(response.data);
      } catch (error) {
        console.error('Error fetching friend:', error);
      } finally {
        setLoading(false);
      }
    };

    if (friendSlug) {
      fetchFriend();
    }
  }, [friendSlug]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-200 to-emerald-400">
        <div className="text-2xl font-semibold text-green-800">Đang tải...</div>
      </div>
    );
  }

  if (!friend) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-200 to-emerald-400">
        <div className="text-2xl font-semibold text-red-600">Không tìm thấy bạn bè!</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-200 to-emerald-400 flex items-center justify-center py-8">
      <div className="bg-white/90 backdrop-blur-sm rounded-3xl shadow-2xl p-12 max-w-lg mx-auto text-center">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Ngày 19/8/2025
          </h1>
          <div className="w-16 h-1 bg-red-500 mx-auto mb-6"></div>
          <p className="text-lg text-red-600 font-semibold leading-relaxed">
            Ngày mà cả thế giới phải chú ý đến
          </p>
        </div>

        <button
          onClick={() => router.push(`/ceremony/${friendSlug}`)}
          className="bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600 text-white font-bold text-2xl px-12 py-4 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
        >
          Tìm hiểu
        </button>
      </div>
    </div>
  );
};

export default InvitationPage;