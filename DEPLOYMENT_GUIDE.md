# 🚀 Complete Deployment Guide

## ✅ Current Status

Your application is **FULLY WORKING** on localhost!

- ✅ **Backend API**: Running at http://localhost:8000
- ✅ **Frontend Website**: Running at http://localhost:3000
- ✅ **Chatbot**: Working perfectly with RAG agent
- ✅ **ADK Agent**: Using Gemini-2.5-flash model
- ✅ **Embeddings**: Pre-generated and loaded
- ✅ **Dark/Light Mode**: Fully functional

---

## 📁 What You Have

### Backend (`backend/` folder)
- `agent.py` - ADK Agent implementation (clean structure)
- `tools.py` - Search tool for embeddings
- `utils.py` - Utility functions with docstrings
- `api.py` - FastAPI server with CORS
- `create_embeddings.py` - Embedding generator
- `embeddings.npy` - Pre-generated embeddings
- `metadata.json` - Chunk metadata
- `requirements.txt` - Python dependencies
- `.env` - Your API key (DO NOT COMMIT!)

### Frontend (`website/` folder)
- `docs/` - 6 complete book chapters
- `src/components/GitChatbot/` - Animated chatbot component
- `src/theme/Root.js` - Global chatbot wrapper
- `docusaurus.config.js` - Docusaurus configuration

---

## 🌐 Deployment Steps

### Option 1: Deploy Backend to Railway (Recommended - Free)

Railway offers free tier for Python applications.

#### Step 1: Create Railway Account

1. Go to https://railway.app
2. Sign up with GitHub
3. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

#### Step 2: Prepare Backend

1. Login to Railway:
   ```bash
   railway login
   ```

2. Navigate to backend:
   ```bash
   cd backend
   ```

3. Initialize Railway project:
   ```bash
   railway init
   ```
   - Choose "Empty Project"
   - Give it a name: "git-book-backend"

#### Step 3: Add Environment Variable

```bash
railway variables set GEMINI_API_KEY=your_actual_api_key_here
```

#### Step 4: Create `railway.json` (Configuration File)

Create a file `backend/railway.json`:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python api.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

#### Step 5: Create `Procfile`

Create a file `backend/Procfile`:

```
web: python api.py
```

#### Step 6: Deploy

```bash
railway up
```

Railway will provide you with a URL like:
`https://git-book-backend-production.up.railway.app`

#### Step 7: Update Frontend API URL

Edit `website/src/components/GitChatbot/index.js`:

```javascript
// Line 16-18
const API_URL = typeof window !== 'undefined' && window.REACT_APP_API_URL 
  ? window.REACT_APP_API_URL 
  : 'https://your-railway-url.railway.app';  // <-- Change this
```

---

### Option 2: Deploy Backend to Render (Alternative - Free)

#### Step 1: Create Render Account

1. Go to https://render.com
2. Sign up with GitHub

#### Step 2: Create Web Service

1. Click "New +"
2. Select "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: git-book-backend
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python api.py`
   - **Instance Type**: Free

#### Step 3: Add Environment Variables

In Render dashboard:
- Key: `GEMINI_API_KEY`
- Value: your_actual_api_key

#### Step 4: Deploy

Click "Create Web Service"

Render will give you a URL like:
`https://git-book-backend.onrender.com`

---

### Deploy Frontend to GitHub Pages

#### Step 1: Update Docusaurus Config

Edit `website/docusaurus.config.js`:

```javascript
// Line 23
url: 'https://yourusername.github.io',

// Line 26
baseUrl: '/Git-for-Non-Developers-Website/',

// Lines 30-31
organizationName: 'yourusername', // Your GitHub username
projectName: 'Git-for-Non-Developers-Website', // Your repo name
```

#### Step 2: Install GH-Pages

```bash
cd website
npm install --save-dev gh-pages
```

#### Step 3: Add Deploy Script to package.json

Edit `website/package.json`, add to scripts:

```json
"scripts": {
  "deploy": "docusaurus deploy",
  "build": "docusaurus build"
}
```

#### Step 4: Build and Deploy

```bash
npm run build
GIT_USER=your-github-username npm run deploy
```

Or use this PowerShell command:
```powershell
$env:GIT_USER="your-github-username"; npm run deploy
```

#### Step 5: Enable GitHub Pages

1. Go to your GitHub repository
2. Settings → Pages
3. Source: Deploy from branch
4. Branch: `gh-pages`
5. Save

Your site will be live at:
`https://yourusername.github.io/Git-for-Non-Developers-Website/`

---

## 🔄 Automated GitHub Actions Deployment

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: npm
          cache-dependency-path: website/package-lock.json
      
      - name: Install dependencies
        run: |
          cd website
          npm ci
      
      - name: Build website
        run: |
          cd website
          npm run build
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./website/build
          user_name: github-actions[bot]
          user_email: github-actions[bot]@users.noreply.github.com
```

Now every push to main will auto-deploy!

---

## 🧪 Testing Deployment

### Test Backend

```bash
curl -X POST "https://your-backend-url.com/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Git?"}'
```

### Test Frontend

1. Visit your GitHub Pages URL
2. Click the chat button (bottom-right)
3. Ask "What is the staging area?"
4. Should get a response from the book

---

## 🐛 Common Issues

### Backend Issues

**Port already in use**
```bash
# Find process on port 8000
netstat -ano | findstr :8000
# Kill it
taskkill /PID <process_id> /F
```

**Module not found**
```bash
cd backend
pip install -r requirements.txt
```

**API key not found**
- Make sure `.env` file exists in backend folder
- Check Railway/Render environment variables

### Frontend Issues

**Build fails**
```bash
cd website
rm -rf node_modules .docusaurus
npm install
npm run build
```

**Chatbot not connecting**
- Check backend URL in `GitChatbot/index.js`
- Verify backend is running
- Check browser console for errors

**GitHub Pages 404**
- Make sure `baseUrl` matches repo name
- Verify `gh-pages` branch exists
- Check GitHub Pages settings

---

## 📊 Monitoring

### Railway
- View logs: `railway logs`
- Open dashboard: `railway open`

### Render
- Logs available in dashboard
- Auto-redeploy on git push

### GitHub Pages
- Check Actions tab for deploy status
- Build logs available in workflow runs

---

## 🔒 Security Checklist

- ✅ `.env` is in `.gitignore`
- ✅ API keys are in environment variables
- ✅ CORS is configured correctly
- ✅ No secrets in frontend code
- ✅ `.env.example` provided for reference

---

## 🎉 You're Done!

Your complete Git learning website with AI chatbot is ready!

**Local URLs:**
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

**Production URLs (after deployment):**
- Backend: https://your-app.railway.app
- Frontend: https://yourusername.github.io/Git-for-Non-Developers-Website/

---

## 📞 Need Help?

1. Check the main README.md
2. Review backend logs: `railway logs` or Render dashboard
3. Check GitHub Actions for frontend deploy errors
4. Test backend with Postman or curl
5. Open browser console for frontend errors

**Happy Deploying! 🚀**
