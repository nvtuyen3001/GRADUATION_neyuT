'use client';

import React, { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import axios from "axios";
import { Friend, GraduationInfo } from "@/lib/models";

const CeremonyPage = () => {
  const { friendSlug } = useParams();
  const [friend, setFriend] = useState<Friend | null>(null);
  const [graduationInfo, setGraduationInfo] = useState<GraduationInfo | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [friendResponse, graduationResponse] = await Promise.all([
          axios.get(`/api/friends/${friendSlug}`),
          axios.get('/api/graduation-info')
        ]);
        setFriend(friendResponse.data);
        setGraduationInfo(graduationResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    if (friendSlug) {
      fetchData();
    }
  }, [friendSlug]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-400 to-emerald-200">
        <div className="text-2xl font-semibold text-green-800">Đang tải...</div>
      </div>
    );
  }

  if (!friend || !graduationInfo) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-400 to-emerald-200">
        <div className="text-2xl font-semibold text-red-600">Không tìm thấy thông tin!</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-400 to-emerald-200 py-8">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="text-sm text-green-800 font-medium mb-2">
            HANOI UNIVERSITY OF INDUSTRY
          </div>
          <div className="text-lg text-green-800 font-bold mb-6">
            HANOI UNIVERSITY OF INDUSTRY
          </div>
        </div>

        {/* Main Card */}
        <div className="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl overflow-hidden max-w-4xl mx-auto">
          {/* Hero Section */}
          <div className="bg-gradient-to-r from-green-400 to-emerald-300 p-8 text-center">
            <h1 className="text-6xl font-bold text-white mb-4 tracking-wide">
              GRADUATION
            </h1>
            <h2 className="text-6xl font-bold text-white mb-4 tracking-wide">
              CEREMONY
              <span className="text-4xl ml-4 text-green-200">2025</span>
            </h2>
            <p className="text-2xl text-white/90 italic font-light">
              Thread of Connection
            </p>
          </div>

          {/* Graduate Info */}
          <div className="p-8 text-center">
            <div className="mb-8">
              <h3 className="text-2xl font-bold text-gray-800 mb-2">
                TÂN CỬ NHÂN
              </h3>
              <h2 className="text-4xl font-bold text-green-800 mb-4">
                {graduationInfo.graduate_name.toUpperCase()}
              </h2>
            </div>

            <div className="mb-8">
              <h4 className="text-xl font-semibold text-gray-700 mb-2">
                CHUYÊN NGÀNH
              </h4>
              <p className="text-2xl text-green-700 font-medium">
                {graduationInfo.major.toUpperCase()}
              </p>
            </div>

            {/* Personalized Message */}
            <div className="bg-gradient-to-r from-green-100 to-emerald-100 rounded-2xl p-6 mb-8">
              <p className="text-xl font-semibold text-green-800 italic">
                This invitation is for: {friend.name}
              </p>
            </div>

            {/* Event Details */}
            <div className="grid md:grid-cols-2 gap-6 text-lg">
              <div className="bg-green-50 rounded-2xl p-6">
                <div className="flex items-center justify-center mb-3">
                  <span className="text-2xl mr-2">⏰</span>
                  <span className="font-bold text-green-800">Thời gian</span>
                </div>
                <p className="text-green-700 font-medium">
                  {graduationInfo.time} - {graduationInfo.date}
                </p>
              </div>

              <div className="bg-emerald-50 rounded-2xl p-6">
                <div className="flex items-center justify-center mb-3">
                  <span className="text-2xl mr-2">📍</span>
                  <span className="font-bold text-green-800">Địa điểm</span>
                </div>
                <p className="text-green-700 font-medium">
                  {graduationInfo.location}
                </p>
              </div>
            </div>

            <div className="mt-6 bg-gradient-to-r from-green-50 to-emerald-50 rounded-2xl p-6">
              <p className="text-green-700 font-medium leading-relaxed mb-2">
                {graduationInfo.address}
              </p>
              <p className="text-green-800 font-semibold text-lg">
                {graduationInfo.university_vietnamese}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CeremonyPage;