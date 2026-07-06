"""
Response Agent.

Responsible for preparing the final API response
returned to the client.
"""

from app.models.response import AgentResponse
from app.tools.logger import logger


class ResponseAgent:
    """
    Autonomous Response Agent.

    Responsibilities:
    - Build the final API response.
    - Return execution summary.
    """

    @staticmethod
    def execute(
        execution_plan: list[str],
        assumptions: list[str],
        document_type: str,
        output_file: str,
    ) -> AgentResponse:
        """
        Build the final API response.

        Parameters
        ----------
        execution_plan : list[str]

        assumptions : list[str]

        document_type : str

        output_file : str

        Returns
        -------
        AgentResponse
        """

        logger.info("Response Agent Started.")

        response = AgentResponse(
            success=True,
            message="Document generated successfully.",
            execution_plan=execution_plan,
            assumptions=assumptions,
            document_type=document_type,
            output_file=output_file,
        )

        logger.info("Response Agent Completed.")

        return response