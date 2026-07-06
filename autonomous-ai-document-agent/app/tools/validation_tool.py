"""
Validation tool for incoming user requests.
"""

from typing import List, Tuple


class RequestValidator:
    """
    Validates incoming user requests before the planner executes.
    """

    MIN_REQUEST_LENGTH = 10
    MAX_REQUEST_LENGTH = 5000

    @classmethod
    def validate(cls, request: str) -> Tuple[bool, List[str]]:
        """
        Validate the user request.

        Returns:
            (is_valid, validation_errors)
        """

        errors: List[str] = []

        # ------------------------------------------------------
        # Empty Request
        # ------------------------------------------------------

        if not request or not request.strip():
            errors.append("Request cannot be empty.")

        # ------------------------------------------------------
        # Minimum Length
        # ------------------------------------------------------

        if len(request.strip()) < cls.MIN_REQUEST_LENGTH:
            errors.append(
                f"Request must contain at least {cls.MIN_REQUEST_LENGTH} characters."
            )

        # ------------------------------------------------------
        # Maximum Length
        # ------------------------------------------------------

        if len(request) > cls.MAX_REQUEST_LENGTH:
            errors.append(
                f"Request exceeds maximum limit of {cls.MAX_REQUEST_LENGTH} characters."
            )

        return len(errors) == 0, errors