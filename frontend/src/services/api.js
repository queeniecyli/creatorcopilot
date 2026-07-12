/**
 * API service for CreatorCopilot frontend
 */

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export class APIError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'APIError';
    this.status = status;
  }
}

/**
 * Generate a campaign using the AI agent
 */
export async function generateCampaign(campaignData) {
  try {
    const response = await fetch(`${API_BASE_URL}/generate-campaign`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(campaignData),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new APIError(
        error.detail || 'Failed to generate campaign',
        response.status
      );
    }

    const data = await response.json();
    return data;
  } catch (error) {
    if (error instanceof APIError) {
      throw error;
    }
    throw new APIError('Network error: ' + error.message, 0);
  }
}

/**
 * Health check
 */
export async function healthCheck() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return await response.json();
  } catch (error) {
    throw new APIError('Health check failed', 0);
  }
}
