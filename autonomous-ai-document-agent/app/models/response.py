"""
Response model for the Autonomous AI Document Agent.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    """
    Standard response returned by the Autonomous AI Agent.
    """

    success: bool = Field(
        ...,
        description="Indicates whether the request was processed successfully."
    )

    message: str = Field(
        ...,
        description="Overall status message."
    )

    execution_plan: List[str] = Field(
        default_factory=list,
        description="Tasks planned by the autonomous agent."
    )

    assumptions: List[str] = Field(
        default_factory=list,
        description="Assumptions made by the agent."
    )

    document_type: Optional[str] = Field(
        default=None,
        description="Generated document type."
    )

    output_file: Optional[str] = Field(
        default=None,
        description="Path of the generated Word document."
    )