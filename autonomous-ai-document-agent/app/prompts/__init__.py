"""
Prompt templates for the Autonomous AI Document Agent.
"""

from app.prompts.planner_prompt import PLANNER_PROMPT
from app.prompts.decision_prompt import DECISION_PROMPT
from app.prompts.executor_prompt import EXECUTOR_PROMPT
from app.prompts.reflection_prompt import REFLECTION_PROMPT

__all__ = [
    "PLANNER_PROMPT",
    "DECISION_PROMPT",
    "EXECUTOR_PROMPT",
    "REFLECTION_PROMPT",
]