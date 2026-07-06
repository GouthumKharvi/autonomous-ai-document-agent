"""
LangGraph State.

Defines the shared state that flows through every node
in the autonomous AI document agent workflow.
"""

from app.models.agent_state import AgentState

# Export the shared state so every LangGraph component
# imports it from a single location.

__all__ = ["AgentState"]