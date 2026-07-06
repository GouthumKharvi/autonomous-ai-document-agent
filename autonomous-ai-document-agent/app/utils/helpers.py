"""
Common helper functions used across the application.
"""

from datetime import datetime
import uuid


def generate_thread_id() -> str:
    """
    Generate a unique thread ID for each agent request.
    """

    return f"thread_{uuid.uuid4().hex}"


def generate_timestamp() -> str:
    """
    Return the current timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_output_filename(document_type: str) -> str:
    """
    Generate a unique DOCX filename.
    """

    safe_name = (
        document_type.strip()
        .lower()
        .replace(" ", "_")
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{safe_name}_{timestamp}.docx"