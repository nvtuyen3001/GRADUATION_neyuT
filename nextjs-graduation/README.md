# Next.js Vietnamese Graduation Invitation Website

A Vietnamese graduation invitation website built with Next.js, TypeScript, Tailwind CSS, and MongoDB.

## Features

- 🎓 **Homepage**: Lists all friends with unique invitation links
- 💌 **Personal Invitation Page**: Shows graduation date with Vietnamese messaging
- 🎊 **Ceremony Details Page**: Displays full ceremony information personalized for each friend
- 🇻🇳 **Vietnamese Language Support**: Full Vietnamese text support with proper slug generation
- 📱 **Responsive Design**: Works on all device sizes
- 🌈 **Beautiful Gradients**: Green to emerald color scheme

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Database**: MongoDB (MongoDB Atlas recommended for production)
- **Deployment**: Optimized for Vercel

## Quick Start

1. **Clone and Install**:
   ```bash
   npm install
   ```

2. **Setup Environment**:
   Copy `.env.example` to `.env.local` and configure:
   ```env
   MONGODB_URI=mongodb://localhost:27017  # For local development
   DB_NAME=graduation_db
   ```

3. **Run Development Server**:
   ```bash
   npm run dev
   ```

4. **Visit**: [http://localhost:3000](http://localhost:3000)

## Deployment on Vercel

### Prerequisites
- MongoDB Atlas account (free tier available)
- Vercel account

### Steps

1. **Setup MongoDB Atlas**:
   - Create a free cluster at [MongoDB Atlas](https://mongodb.com/atlas)
   - Create a database user
   - Whitelist Vercel's IP addresses (or use 0.0.0.0/0 for all IPs)
   - Get your connection string

2. **Deploy to Vercel**:
   ```bash
   # Install Vercel CLI
   npm i -g vercel

   # Deploy
   vercel
   ```

3. **Configure Environment Variables in Vercel**:
   - Go to your project in Vercel Dashboard
   - Navigate to Settings → Environment Variables
   - Add:
     ```
     MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
     DB_NAME=graduation_db
     ```

4. **Redeploy**:
   ```bash
   vercel --prod
   ```

## API Endpoints

- `GET /api/friends` - Get all friends
- `POST /api/friends` - Create a new friend
- `GET /api/friends/[slug]` - Get friend by slug
- `GET /api/graduation-info` - Get graduation ceremony information
- `POST /api/init-data` - Initialize sample Vietnamese friends data

## Project Structure

```
src/
├── app/
│   ├── api/                    # API routes
│   │   ├── friends/
│   │   ├── graduation-info/
│   │   └── init-data/
│   ├── invite/[friendSlug]/    # Personal invitation pages
│   ├── ceremony/[friendSlug]/  # Ceremony detail pages
│   └── page.tsx                # Homepage
├── lib/
│   ├── mongodb.ts              # MongoDB connection
│   └── models.ts               # TypeScript interfaces and utilities
```

## Features Included

- **Vietnamese Text Processing**: Automatic slug generation for Vietnamese names
- **Sample Data**: Pre-loaded with Vietnamese friend names
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Type Safety**: Full TypeScript implementation
- **SEO Ready**: Next.js App Router with proper meta tags
- **Serverless Optimized**: Ready for Vercel's edge functions

## Customization

- **Graduation Info**: Edit in `/src/app/api/graduation-info/route.ts`
- **Sample Friends**: Modify in `/src/app/api/init-data/route.ts`
- **Styling**: Update Tailwind classes in component files
- **Colors**: Change gradient colors in the components

## Performance

- ✅ Optimized for Vercel's Edge Runtime
- ✅ Automatic code splitting
- ✅ MongoDB connection pooling for serverless
- ✅ Static generation where possible
- ✅ Image optimization ready

## License

MIT License
