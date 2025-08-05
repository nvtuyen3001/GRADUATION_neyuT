# Deployment Guide for Vercel

## Quick Deploy Steps

### Prerequisites
- MongoDB Atlas account (free tier available)
- Vercel account  
- GitHub account

### Step 1: Setup MongoDB Atlas

1. **Create Atlas Account**: Go to [mongodb.com/atlas](https://mongodb.com/atlas)

2. **Create a Free Cluster**:
   - Choose Free Tier (M0 Sandbox)
   - Select a region close to your users
   - Create cluster

3. **Setup Database Access**:
   - Go to Database Access
   - Add Database User
   - Choose "Password" authentication
   - Create username/password (save these!)
   - Give "readWrite" permissions to built-in role

4. **Setup Network Access**:
   - Go to Network Access → Add IP Address
   - Choose "Allow Access from Anywhere" (0.0.0.0/0)
   - Or add Vercel's IP ranges

5. **Get Connection String**:
   - Go to Database → Connect
   - Choose "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your actual password
   - Should look like: `mongodb+srv://username:password@cluster.mongodb.net/`

### Step 2: Deploy to Vercel

#### Option A: Deploy via Vercel Dashboard (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Vietnamese graduation invitation Next.js app"
   git branch -M main
   git remote add origin https://github.com/yourusername/nextjs-graduation.git
   git push -u origin main
   ```

2. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - **Root Directory**: Leave as `.` (root)
   - Vercel will auto-detect Next.js

3. **Set Environment Variables**:
   - In project settings, go to Environment Variables
   - Add these:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
   DB_NAME=graduation_db
   NODE_ENV=production
   ```

4. **Deploy**: Click Deploy!

#### Option B: Deploy via CLI

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Set Environment Variables**:
   ```bash
   vercel env add MONGODB_URI production
   vercel env add DB_NAME production
   vercel env add NODE_ENV production
   ```

5. **Redeploy**:
   ```bash
   vercel --prod
   ```

### Step 3: Verify Deployment

After successful deployment:

1. **Visit your site**: `https://yourapp.vercel.app`
2. **Test API**: Visit `https://yourapp.vercel.app/api/friends`
3. **Initialize data**: POST to `https://yourapp.vercel.app/api/init-data`
4. **Test navigation**: Click on friend names

### Environment Variables Reference

```env
# Production (Vercel)
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=graduation_db
NODE_ENV=production
```

```env
# Development (.env.local)
MONGODB_URI=mongodb://localhost:27017
DB_NAME=graduation_db
NODE_ENV=development
```

### Common Issues & Solutions

**"No Next.js version detected"**
- ✅ Fixed: package.json is now in root directory

**MongoDB Connection Issues**
- Ensure URI format is correct
- Check database user permissions
- Verify network access (0.0.0.0/0)
- Use MongoDB Atlas connection string, not local

**Environment Variables Not Working**
- Double-check variable names (case sensitive)
- Redeploy after adding variables
- No trailing spaces in values

**Build/Deployment Fails**
- Check Vercel build logs
- Ensure all dependencies are in package.json
- Verify TypeScript compilation

### Features After Deployment

- ✅ Homepage with Vietnamese friends list
- ✅ Personal invitation pages with routing
- ✅ Ceremony detail pages with full info
- ✅ Vietnamese text processing and slugs
- ✅ Responsive design on all devices
- ✅ Serverless APIs on Vercel Edge Functions
- ✅ MongoDB Atlas integration
- ✅ Automatic HTTPS and global CDN

### Custom Domain (Optional)

1. In Vercel dashboard: Settings → Domains
2. Add your domain
3. Configure DNS as instructed

Your Vietnamese graduation invitation website is now live on Vercel! 🎓