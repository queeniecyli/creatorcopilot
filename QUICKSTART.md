# Quick Start Guide

Get CreatorCopilot running in 5 minutes!

## 1. Get Your API Keys

### Required:
- **Anthropic API Key**: https://console.anthropic.com/
  - Sign up and create an API key
  - You'll get $5 free credit to start

### Optional:
- **SerpAPI Key**: https://serpapi.com/
  - For real trend data (app works without it using mock data)
  - Free tier: 100 searches/month

## 2. Backend Setup (Terminal 1)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your API key
# ANTHROPIC_API_KEY=sk-ant-...
# SERPAPI_KEY=...  (optional)

# Start server
python -m uvicorn app.main:app --reload
```

Backend now running at **http://localhost:8000**

## 3. Frontend Setup (Terminal 2)

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend now running at **http://localhost:5173**

## 4. Test It!

1. Open **http://localhost:5173**
2. Fill in the form:
   - Business: "Sakura Ramen House"
   - Industry: "Japanese restaurant"
   - Location: "Sydney"
   - Platform: "TikTok"
   - Objective: "Increase awareness"
   - Audience: "Sydney food lovers"
   - Tone: "Authentic, casual"

3. Click "Generate Campaign Strategy"
4. Wait 10-30 seconds
5. See your AI-generated campaign! 🎉

## Troubleshooting

### Backend won't start
- Check you activated the virtual environment
- Verify ANTHROPIC_API_KEY in .env file
- Try: `pip install --upgrade anthropic`

### Frontend won't start
- Check Node.js version: `node --version` (need 18+)
- Delete `node_modules` and run `npm install` again
- Check port 5173 isn't in use

### "API Error" in browser
- Check backend is running (http://localhost:8000/docs)
- Check CORS settings in backend/app/main.py
- Verify API key is valid

### Generation takes forever
- Normal: 10-30 seconds
- Check your internet connection
- Check Anthropic API status: https://status.anthropic.com/

### "Tool execution error"
- This is OK if you don't have SERPAPI_KEY
- App will use mock data for trends
- Real SerpAPI key improves quality

## Next Steps

- Try different businesses and platforms
- Experiment with different tones
- Read the full README.md for deployment info
- Check out the code to understand the AI agent architecture!

## Quick Commands Reference

```bash
# Backend
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload

# Frontend
cd frontend
npm run dev

# View API docs
open http://localhost:8000/docs
```

Happy creating! 🎬✨
