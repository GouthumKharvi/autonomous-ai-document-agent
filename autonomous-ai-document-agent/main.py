"""
Application Entry Point.

Starts the FastAPI server for the Autonomous AI Document Agent.
"""

from fastapi import FastAPI

from app.api import router


app = FastAPI(
    title="Autonomous AI Document Agent",
    description="An AI-powered autonomous system for generating professional business documents.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/", tags=["Health"])
def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "success",
        "message": "Autonomous AI Document Agent is running."
    }