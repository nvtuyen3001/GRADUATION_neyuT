import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Lễ Tốt Nghiệp 2025 - Nguyen Van Tuyen",
  description: "Website thiệp mời tốt nghiệp tiếng Việt - Lễ tốt nghiệp Nguyễn Văn Tuyền 2025",
  keywords: "tốt nghiệp, thiệp mời, Việt Nam, graduation, invitation",
  openGraph: {
    title: "Lễ Tốt Nghiệp 2025 - Nguyen Van Tuyen",
    description: "Mời các bạn tham dự lễ tốt nghiệp",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="vi">
      <body className={inter.className}>{children}</body>
    </html>
  );
}