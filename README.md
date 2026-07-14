# CreatorCopilot

AI-powered content strategy agent for social media campaigns, built with OpenAI GPT-4o and function calling.

## Overview

CreatorCopilot is an intelligent AI agent that helps content creators and small businesses generate high-performing social media campaigns. Built as a personal portfolio project, this tool has personally boosted my productivity as a content creator by automating the time-consuming process of brainstorming, trend research, and campaign planning.

### Key Features

- **AI Agent Architecture**: Uses OpenAI function calling for autonomous workflow orchestration
- **Tool Use**: AI autonomously determines when to research trends via SerpAPI
- **Complete Campaign Generation**: Scripts, hooks, shot lists, captions, hashtags, and optimisation tips
- **Platform-Specific**: Optimised for TikTok, Instagram Reels, and YouTube Shorts
- **Trend-Grounded**: Uses real search data to inform content strategy

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **OpenAI GPT-4o**: Latest multimodal model with 128K context window
- **OpenAI Function Calling**: For building reliable AI agents
- **SerpAPI**: For real-time trend research
- **Python 3.10+**

### Frontend
- **React 18**: Modern UI library
- **Vite**: Fast build tool
- **Tailwind CSS**: Utility-first styling
- **ES6+**: Modern JavaScript

## Project Structure

```
creatorcopilot/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── agent/
│   │   │   ├── creator_agent.py # OpenAI agent with function calling
│   │   │   ├── tools.py         # Tool definitions (SerpAPI)
│   │   │   └── prompts.py       # System prompts
│   │   └── api/
│   │       └── routes.py        # API endpoints
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Generator.jsx    # Campaign input form
│   │   │   └── Results.jsx      # Campaign results display
│   │   ├── services/
│   │   │   └── api.js           # API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- SerpAPI key (optional, for real trend data - [get one here](https://serpapi.com/))

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp .env.example .env
```

5. Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_actual_openai_api_key
SERPAPI_KEY=your_serpapi_key  # Optional - will use mock data if not provided
FRONTEND_URL=http://localhost:5173
ENVIRONMENT=development
```

6. Run the backend:
```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Usage

1. Open http://localhost:5173 in your browser
2. Fill in the campaign details:
   - Business name and industry
   - Location and target audience
   - Social media platform
   - Campaign objective
   - Brand tone

3. Click "Generate Campaign Strategy"

4. The AI agent will:
   - Research trending topics using SerpAPI
   - Analyze your business context
   - Generate a complete campaign package

5. Review your results:
   - Campaign concept and content angle
   - Attention-grabbing video hook
   - Full 30-60 second script
   - Detailed shot list
   - Engaging caption
   - Relevant hashtags
   - Call-to-action
   - Platform-specific optimisation tips

## API Documentation

### Endpoints

#### POST `/api/generate-campaign`

Generate a complete campaign strategy.

**Request Body:**
```json
{
  "business_name": "Sakura Ramen House",
  "industry": "Japanese restaurant",
  "location": "Sydney",
  "platform": "TikTok",
  "objective": "Increase restaurant awareness",
  "audience": "Sydney food lovers aged 18-35",
  "tone": "Authentic, casual, engaging"
}
```

**Response:**
```json
{
  "campaign_name": "Behind the Scenes: Authentic Ramen",
  "content_angle": "Show traditional ramen-making process",
  "hook": "POV: You're about to discover why...",
  "script": "Full 30-60 second script...",
  "shot_list": [
    "Close-up: Chef hand-pulling noodles",
    "Wide shot: Kitchen atmosphere",
    "Close-up: Broth simmering"
  ],
  "caption": "Engaging caption with storytelling...",
  "hashtags": ["#SydneyEats", "#RamenLovers", "#AuthenticJapanese"],
  "cta": "Visit us at [location]",
  "recommendations": [
    "Post during peak engagement hours (6-9 PM)",
    "Use trending audio related to cooking/ASMR"
  ]
}
```

#### GET `/api/health`

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "CreatorCopilot API",
  "version": "1.0.0"
}
```

## How It Works

### AI Agent Workflow

```
User Input → Business Context Analysis
     ↓
Agent Determines Required Actions
     ↓
Tool 1: Trend Research (SerpAPI)
     ↓
Tool 2: Content Strategy Generation
     ↓
Structured Campaign Output
```

### Agent Architecture

The CreatorCopilot agent uses OpenAI's function calling capability to autonomously:

1. **Analyze** the business context and campaign requirements
2. **Decide** to use the trend research tool
3. **Execute** the SerpAPI search to gather trending topics
4. **Synthesize** trend data with business context
5. **Generate** a complete, platform-optimised campaign strategy

This demonstrates true agent behaviour, not just simple LLM prompting.

## Why OpenAI GPT-4o?

I chose OpenAI GPT-4o with function calling for several reasons:

- **Advanced Function Calling**: Excellent at autonomous decision-making and tool orchestration
- **Global Availability**: Broad regional support including Australia
- **Content Quality**: Exceptional performance in creative content and marketing copy
- **Production-Ready**: Mature API with extensive documentation and reliability
- **Cost Efficiency**: Competitive pricing suitable for both prototyping and production

## Development Notes

### Testing Without API Keys

The application includes mock data fallbacks:
- If no `SERPAPI_KEY` is provided, the trend research tool returns sample data
- This allows you to test the full workflow without API costs

### Error Handling

- Backend validates all inputs and returns structured error responses
- Frontend displays user-friendly error messages
- Tool execution errors are caught and don't crash the agent

### Performance

- Backend uses async/await for concurrent API calls
- Frontend shows loading states during generation
- Typical generation time: 10-30 seconds

## Deployment

### Backend (Render/AWS)

1. Set environment variables in platform dashboard
2. Deploy from Git repository
3. Ensure health check endpoint is configured

### Frontend (Vercel)

1. Connect Git repository
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Add environment variable: `VITE_API_URL=https://your-backend-url.com/api`

## Future Enhancements

- Multi-platform campaign generation (all platforms at once)
- Image generation integration (DALL-E for thumbnails)
- Campaign history and iteration
- A/B testing recommendations
- Performance prediction ML models
- Export to PDF/presentation formats
