# Next.js Vietnamese Graduation Invitation Website

A Vietnamese graduation invitation website built with Next.js, TypeScript, Tailwind CSS, and MongoDB - optimized for **Vercel deployment**.

## ✨ Features

- 🎓 **Homepage**: Lists all friends with unique invitation links
- 💌 **Personal Invitation Page**: Shows graduation date with Vietnamese messaging  
- 🎊 **Ceremony Details Page**: Displays full ceremony information personalized for each friend
- 🇻🇳 **Vietnamese Language Support**: Full Vietnamese text support with proper slug generation
- 📱 **Responsive Design**: Works perfectly on all device sizes
- 🌈 **Beautiful Gradients**: Green to emerald color scheme

## 🚀 Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **Database**: MongoDB (MongoDB Atlas for production)
- **Deployment**: Optimized for Vercel
- **APIs**: Next.js API Routes (serverless)

## 📦 Quick Start

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Setup Environment**:
   Copy `.env.example` to `.env.local`:
   ```env
   MONGODB_URI=mongodb://localhost:27017
   DB_NAME=graduation_db
   NODE_ENV=development
   ```

3. **Run Development Server**:
   ```bash
   npm run dev
   ```

4. **Visit**: [http://localhost:3000](http://localhost:3000)

## 🌐 Deploy on Vercel

### Quick Deploy:
1. Push to GitHub
2. Connect to Vercel  
3. Set environment variables
4. Deploy! 🚀

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.

### Environment Variables for Vercel:
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=graduation_db
NODE_ENV=production
```

## 🔄 API Endpoints

- `GET /api/friends` - Get all friends
- `POST /api/friends` - Create a new friend  
- `GET /api/friends/[slug]` - Get friend by slug
- `GET /api/graduation-info` - Get graduation ceremony information
- `POST /api/init-data` - Initialize sample Vietnamese friends data

## 📁 Project Structure

```
/app/                           # Root directory (ready for Vercel)
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── api/               # API Routes (replaces FastAPI)
│   │   │   ├── friends/
│   │   │   ├── graduation-info/
│   │   │   └── init-data/
│   │   ├── invite/[friendSlug]/ # Personal invitation pages
│   │   ├── ceremony/[friendSlug]/ # Ceremony detail pages
│   │   ├── page.tsx           # Homepage
│   │   └── layout.tsx         # Root layout
│   └── lib/
│       ├── mongodb.ts         # MongoDB connection (serverless optimized)
│       └── models.ts          # TypeScript interfaces
├── package.json               # Dependencies (Next.js detected ✅)
├── next.config.js             # Next.js configuration
├── vercel.json                # Vercel deployment config
├── .env.local                 # Development environment
├── .env.example               # Production template
└── DEPLOYMENT.md              # Vercel deployment guide
```

## ✅ Production Ready

- ✅ **Vercel Optimized**: Package.json in root, serverless functions ready
- ✅ **MongoDB Atlas**: Serverless database connection pooling
- ✅ **TypeScript**: Full type safety and autocomplete
- ✅ **SEO Ready**: Next.js App Router with proper meta tags
- ✅ **Performance**: Automatic code splitting and optimization
- ✅ **Vietnamese Support**: Proper Unicode handling and slug generation

## 🎨 Customization

- **Graduation Info**: Edit `/src/app/api/graduation-info/route.ts`
- **Sample Friends**: Modify `/src/app/api/init-data/route.ts`  
- **Styling**: Update Tailwind classes in component files
- **Colors**: Change gradient colors in the page components

## 🧪 Testing

Build and test production:
```bash
npm run build
npm start
```

Test APIs:
```bash
curl -X POST http://localhost:3000/api/init-data
curl http://localhost:3000/api/friends
```

## 🚀 Features After Deployment

- Vietnamese graduation invitation with 11 sample friends
- Dynamic routing: `/invite/ha-nguyen-tuan-kiet`  
- Personalized ceremony pages
- Mobile-responsive design
- Automatic HTTPS and global CDN via Vercel
- Serverless APIs with zero cold start

## 📄 License

MIT License

---

Ready to deploy your Vietnamese graduation invitation website! 🎓✨
