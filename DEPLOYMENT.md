# Deployment Guide for Vercel

## Option 1: Direct Vercel Deployment (Recommended)

1. **Push to GitHub** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Vietnamese graduation invitation website"
   git remote add origin https://github.com/yourusername/nextjs-graduation.git
   git push -u origin main
   ```

2. **Deploy via Vercel Dashboard**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect Next.js settings

3. **Set Environment Variables in Vercel**:
   - In your Vercel project dashboard
   - Go to Settings → Environment Variables
   - Add these variables:
     ```
     Name: MONGODB_URI
     Value: mongodb+srv://username:password@cluster.mongodb.net/
     
     Name: DB_NAME  
     Value: graduation_db
     ```

## Option 2: CLI Deployment

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Set Environment Variables**:
   ```bash
   vercel env add MONGODB_URI
   vercel env add DB_NAME
   ```

5. **Redeploy with environment variables**:
   ```bash
   vercel --prod
   ```

## MongoDB Atlas Setup

1. **Create Atlas Account**: Go to [mongodb.com/atlas](https://mongodb.com/atlas)

2. **Create a Cluster**:
   - Choose Free Tier (M0)
   - Select a region close to your users
   - Create cluster

3. **Setup Database Access**:
   - Go to Database Access
   - Add Database User
   - Choose "Password" authentication
   - Create username/password
   - Give "readWrite" permissions

4. **Setup Network Access**:
   - Go to Network Access
   - Add IP Address
   - For Vercel, use `0.0.0.0/0` (allow access from anywhere)
   - Or add Vercel's specific IP ranges

5. **Get Connection String**:
   - Go to Database → Connect
   - Choose "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your actual password

## Environment Variables Format

For **Development** (`.env.local`):
```env
MONGODB_URI=mongodb://localhost:27017
DB_NAME=graduation_db
NODE_ENV=development
```

For **Production** (Vercel Environment Variables):
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=graduation_db
NODE_ENV=production
```

## Verification Steps

After deployment:

1. **Check Homepage**: Your site should load at `https://yourapp.vercel.app`
2. **Test API**: Visit `https://yourapp.vercel.app/api/friends` 
3. **Initialize Data**: POST to `https://yourapp.vercel.app/api/init-data`
4. **Test Navigation**: Try clicking on friend names to test routing

## Common Issues & Solutions

### MongoDB Connection Issues
- Ensure your MongoDB URI is correct
- Check that your database user has proper permissions
- Verify that 0.0.0.0/0 is whitelisted in Network Access

### Environment Variables Not Loading
- Double-check variable names in Vercel dashboard
- Redeploy after adding environment variables
- Ensure no trailing spaces in values

### 500 Errors in Production
- Check Vercel Function Logs in dashboard
- Verify MongoDB connection string format
- Ensure database name matches your MongoDB setup

## Performance Optimization

- MongoDB Atlas provides automatic scaling
- Vercel Edge Functions are optimized for fast cold starts
- Consider enabling MongoDB connection pooling for high traffic

## Custom Domain (Optional)

1. In Vercel dashboard, go to Settings → Domains
2. Add your custom domain
3. Configure DNS records as instructed by Vercel