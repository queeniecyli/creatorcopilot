"""
API routes for CreatorCopilot
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from ..agent.creator_agent import get_agent


router = APIRouter()


class CampaignRequest(BaseModel):
    """Request model for campaign generation."""
    business_name: str = Field(..., description="Name of the business")
    industry: str = Field(..., description="Industry or category")
    location: str = Field(..., description="Geographic location")
    platform: str = Field(..., description="Social media platform (TikTok, Instagram, YouTube)")
    objective: str = Field(..., description="Campaign objective")
    audience: str = Field(..., description="Target audience description")
    tone: str = Field(..., description="Brand tone (e.g., authentic, casual, professional)")


class CampaignResponse(BaseModel):
    """Response model for campaign generation."""
    campaign_name: Optional[str] = None
    content_angle: Optional[str] = None
    hook: Optional[str] = None
    script: Optional[str] = None
    shot_list: Optional[list[str]] = None
    caption: Optional[str] = None
    hashtags: Optional[list[str]] = None
    cta: Optional[str] = None
    recommendations: Optional[list[str]] = None
    error: Optional[str] = None


@router.post("/generate-campaign", response_model=CampaignResponse)
async def generate_campaign(request: CampaignRequest):
    """
    Generate a complete social media campaign strategy.

    Args:
        request: Campaign generation request

    Returns:
        Complete campaign strategy with script, shots, captions, etc.
    """
    try:
        agent = get_agent()

        result = await agent.generate_campaign(
            business_name=request.business_name,
            industry=request.industry,
            location=request.location,
            platform=request.platform,
            objective=request.objective,
            audience=request.audience,
            tone=request.tone
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Campaign generation failed: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "CreatorCopilot API",
        "version": "1.0.0"
    }
