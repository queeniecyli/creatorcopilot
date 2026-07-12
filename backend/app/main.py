"""
CreatorCopilot FastAPI Application
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .api.routes import router

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="CreatorCopilot API",
    description="AI-powered content strategy agent for social media campaigns",
    version="1.0.0"
)

# Configure CORS
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "CreatorCopilot API",
        "version": "1.0.0",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
