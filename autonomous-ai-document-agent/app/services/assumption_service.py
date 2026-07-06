"""
Assumption Service.

Generates reasonable assumptions for missing information
based on the selected document type.
"""

from typing import List

from app.tools.mock_data_tool import MockDataProvider


class AssumptionService:
    """
    Builds assumptions using document-specific mock data.
    """

    @staticmethod
    def generate_assumptions(document_type: str) -> List[str]:
        """
        Generate assumptions based on document type.

        Parameters
        ----------
        document_type : str

        Returns
        -------
        List[str]
        """

        mock_data = MockDataProvider.get_mock_data(document_type)

        assumptions = []

        for key, value in mock_data.items():

            if isinstance(value, list):
                continue

            formatted_key = key.replace("_", " ").title()

            assumptions.append(
                f"{formatted_key}: {value}"
            )

        return assumptions