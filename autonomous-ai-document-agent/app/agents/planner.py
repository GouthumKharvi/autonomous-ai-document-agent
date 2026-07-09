"""
Planner Agent.

Responsible for analyzing the user's request and generating
an execution plan for the autonomous workflow.
"""

from app.services.gemini_service import GeminiService
from app.services.prompt_builder import PromptBuilder
from app.tools.logger import logger


class PlannerAgent:
    """
    Autonomous Planner Agent.

    Responsibilities:
    - Understand the user's request.
    - Break the request into logical execution steps.
    - Return a structured execution plan.
    """

    def __init__(self) -> None:
        self.llm = GeminiService()

    def execute(self, request: str) -> list[str]:
        """
        Generate an execution plan for the given request.

        Parameters
        ----------
        request : str
            User's natural language request.

        Returns
        -------
        list[str]
            Ordered list of execution steps.
        """

        logger.info("Planner Agent Started.")

        prompt = PromptBuilder.build_planner_prompt(request)

        response = self.llm.invoke(prompt)

        execution_plan: list[str] = []

        step_number = 1

        for line in response.splitlines():

            line = line.strip()

            if not line:
                continue

            execution_plan.append(
                f"Step {step_number}: {line} | Status: Pending"
            )

            step_number += 1

        logger.info(
            "Planner Agent Completed. Generated %d execution steps.",
            len(execution_plan),
        )

        return execution_plan