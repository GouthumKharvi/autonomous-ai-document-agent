"""
Request model for the Autonomous AI Document Agent.
"""

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """
    Incoming request for the autonomous AI agent.
    """

    request: str = Field(
        ...,
        min_length=5,
        max_length=5000,
        description="Natural language request provided by the user."
    )