"""
Executor Agent.

Responsible for generating the final document content
using the selected document type and assumptions.
"""

from app.services.gemini_service import GeminiService
from app.services.prompt_builder import PromptBuilder
from app.tools.logger import logger


class ExecutorAgent:
    """
    Autonomous Executor Agent.

    Responsibilities:
    - Generate professional document content.
    - Use assumptions when required.
    """

    def __init__(self) -> None:
        self.llm = GeminiService()

    def execute(
        self,
        request: str,
        document_type: str,
        assumptions: list[str],
    ) -> str:
        """
        Generate the final document.

        Parameters
        ----------
        request : str
            User request.

        document_type : str
            Selected document type.

        assumptions : list[str]
            Generated assumptions.

        Returns
        -------
        str
            Generated document content.
        """

        logger.info("Executor Agent Started.")

        prompt = PromptBuilder.build_executor_prompt(
            request=request,
            document_type=document_type,
            assumptions=assumptions,
        )

        generated_content = self.llm.invoke(prompt)

        logger.info("Executor Agent Completed.")

        return generated_content