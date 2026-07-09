"""
API Routes.

Defines REST API endpoints for the Autonomous AI Document Agent.
"""

from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.graph import AutonomousDocumentGraph
from app.graph.memory import GraphMemory
from app.models.request import AgentRequest
from app.tools.logger import logger

router = APIRouter(
    prefix="/api/v1",
    tags=["Autonomous AI Document Agent"],
)

graph = AutonomousDocumentGraph().get_graph()


@router.post("/generate")
def generate_document(request: AgentRequest):
    """
    Generate a business document using the autonomous AI agent.
    """

    logger.info("Received document generation request.")

    try:

        # Generate a unique thread id for conversation memory
        thread_id = str(uuid4())

        # Initial LangGraph state
        initial_state = {
            "request": request.request,
            "thread_id": thread_id,
        }

        # Execute LangGraph workflow
        result = graph.invoke(
            initial_state,
            config=GraphMemory.get_config(thread_id),
        )

        logger.info("Document generated successfully.")

        return result

    except Exception as error:

        logger.exception("Document generation failed: %s", error)

        raise HTTPException(
            status_code=500,
            detail="Failed to generate document.",
        )