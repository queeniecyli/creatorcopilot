"""
Tool definitions for CreatorCopilot AI Agent
"""
import httpx
import json
import os
from typing import Dict, List, Any


async def search_trends(query: str, location: str = "Sydney") -> Dict[str, Any]:
    """
    Search for trending topics and keywords using SerpAPI.

    Args:
        query: The search query (e.g., "Japanese restaurant")
        location: Geographic location for trends (default: Sydney)

    Returns:
        Dictionary containing trending keywords, related searches, and popular topics
    """
    serpapi_key = os.getenv("SERPAPI_KEY")

    # If no API key, return mock data for development
    if not serpapi_key or serpapi_key == "your_serpapi_key_here":
        return {
            "trending_keywords": [
                f"{query} near me",
                f"best {query} {location}",
                f"{query} delivery",
                f"authentic {query}",
            ],
            "related_searches": [
                f"{query} reviews",
                f"{query} menu",
                f"top rated {query}",
            ],
            "popular_topics": [
                "behind the scenes content",
                "food preparation videos",
                "customer testimonials",
                "chef stories",
            ],
            "note": "Mock data - add SERPAPI_KEY for real trend data"
        }

    # Real SerpAPI implementation
    try:
        async with httpx.AsyncClient() as client:
            params = {
                "api_key": serpapi_key,
                "q": f"{query} {location}",
                "location": location,
                "engine": "google"
            }

            response = await client.get(
                "https://serpapi.com/search",
                params=params,
                timeout=10.0
            )

            if response.status_code == 200:
                data = response.json()

                # Extract trending information from search results
                trending_keywords = []
                related_searches = []

                # Get related searches
                if "related_searches" in data:
                    related_searches = [
                        item.get("query", "")
                        for item in data["related_searches"][:5]
                    ]

                # Get people also ask
                if "related_questions" in data:
                    trending_keywords = [
                        item.get("question", "")
                        for item in data["related_questions"][:5]
                    ]

                return {
                    "trending_keywords": trending_keywords,
                    "related_searches": related_searches,
                    "popular_topics": [
                        "viral content trends",
                        "engaging storytelling formats",
                        "platform-specific best practices"
                    ],
                    "source": "SerpAPI"
                }
            else:
                # Fallback to mock data if API fails
                return {
                    "trending_keywords": [f"{query} {location} trends"],
                    "related_searches": [f"popular {query}"],
                    "popular_topics": ["trending content"],
                    "error": f"SerpAPI returned status {response.status_code}"
                }

    except Exception as e:
        # Fallback to mock data on error
        return {
            "trending_keywords": [f"{query} content ideas"],
            "related_searches": [f"{query} marketing"],
            "popular_topics": ["social media trends"],
            "error": f"SerpAPI error: {str(e)}"
        }


# Tool definitions for Claude (legacy)
TOOLS = [
    {
        "name": "search_trends",
        "description": "Search for trending topics, keywords, and popular content ideas related to a business or industry. Use this to ground content strategy in real search behavior and current trends.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The business type or topic to search for (e.g., 'Japanese restaurant', 'coffee shop')"
                },
                "location": {
                    "type": "string",
                    "description": "Geographic location for localized trends (e.g., 'Sydney', 'Melbourne')"
                }
            },
            "required": ["query"]
        }
    }
]

# Tool definitions for OpenAI
TOOLS_OPENAI = [
    {
        "type": "function",
        "function": {
            "name": "search_trends",
            "description": "Search for trending topics, keywords, and popular content ideas related to a business or industry. Use this to ground content strategy in real search behavior and current trends.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The business type or topic to search for (e.g., 'Japanese restaurant', 'coffee shop')"
                    },
                    "location": {
                        "type": "string",
                        "description": "Geographic location for localized trends (e.g., 'Sydney', 'Melbourne')"
                    }
                },
                "required": ["query"]
            }
        }
    }
]


async def execute_tool(tool_name: str, tool_input: Dict[str, Any]) -> Any:
    """
    Execute a tool by name with given input.

    Args:
        tool_name: Name of the tool to execute
        tool_input: Input parameters for the tool

    Returns:
        Tool execution result
    """
    if tool_name == "search_trends":
        return await search_trends(**tool_input)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")
