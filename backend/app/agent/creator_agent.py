"""
CreatorCopilot AI Agent using OpenAI with function calling
"""
import json
import os
from typing import Dict, Any, List
from openai import OpenAI
from .tools import TOOLS_OPENAI, execute_tool
from .prompts import CREATOR_STRATEGIST_PROMPT, get_campaign_generation_prompt


class CreatorAgent:
    """
    AI Agent for generating content strategy using OpenAI with function calling.
    """

    def __init__(self):
        """Initialize the OpenAI client."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")

        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o"
        self.max_tokens = 4096

    async def generate_campaign(
        self,
        business_name: str,
        industry: str,
        location: str,
        platform: str,
        objective: str,
        audience: str,
        tone: str
    ) -> Dict[str, Any]:
        """
        Generate a complete social media campaign strategy.

        Args:
            business_name: Name of the business
            industry: Industry/category
            location: Geographic location
            platform: Social media platform
            objective: Campaign objective
            audience: Target audience
            tone: Brand tone

        Returns:
            Dictionary containing campaign strategy
        """
        # Build the user prompt
        user_prompt = get_campaign_generation_prompt(
            business_name=business_name,
            industry=industry,
            location=location,
            platform=platform,
            objective=objective,
            audience=audience,
            tone=tone
        )

        messages = [
            {"role": "system", "content": CREATOR_STRATEGIST_PROMPT},
            {"role": "user", "content": user_prompt}
        ]

        # Agent loop: allow OpenAI to use tools
        max_iterations = 5
        iteration = 0

        while iteration < max_iterations:
            iteration += 1

            # Call OpenAI with function calling
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=messages,
                tools=TOOLS_OPENAI,
                tool_choice="auto"
            )

            message = response.choices[0].message

            # Check if we're done (got final response)
            if message.tool_calls is None:
                # Extract the final text response
                final_text = message.content or ""

                # Try to parse as JSON
                try:
                    # Find JSON in the response
                    json_start = final_text.find("{")
                    json_end = final_text.rfind("}") + 1

                    if json_start != -1 and json_end > json_start:
                        json_str = final_text[json_start:json_end]
                        campaign_data = json.loads(json_str)
                        return campaign_data
                    else:
                        # If no JSON found, return structured response
                        return {
                            "campaign_name": "Custom Campaign",
                            "content_angle": final_text[:200],
                            "response": final_text,
                            "error": "Could not parse JSON from response"
                        }
                except json.JSONDecodeError as e:
                    return {
                        "error": f"JSON parse error: {str(e)}",
                        "raw_response": final_text
                    }

            # OpenAI wants to use tools
            else:
                # Add assistant's response to messages
                messages.append(message)

                # Execute tools and collect results
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_input = json.loads(tool_call.function.arguments)

                    print(f"Agent calling tool: {tool_name} with input: {tool_input}")

                    # Execute the tool
                    try:
                        result = await execute_tool(tool_name, tool_input)
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps(result)
                        })
                    except Exception as e:
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps({"error": str(e)})
                        })

        # Max iterations reached
        return {
            "error": "Max iterations reached without completion",
            "iterations": iteration
        }


# Singleton instance
_agent_instance = None


def get_agent() -> CreatorAgent:
    """Get or create the singleton agent instance."""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = CreatorAgent()
    return _agent_instance
