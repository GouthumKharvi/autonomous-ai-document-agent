"""
Custom exceptions used throughout the application.
"""


class AgentException(Exception):
    """
    Base exception for the Autonomous AI Document Agent.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class ValidationException(AgentException):
    """
    Raised when request validation fails.
    """
    pass


class PlanningException(AgentException):
    """
    Raised when the planner fails to generate an execution plan.
    """
    pass


class DecisionException(AgentException):
    """
    Raised when the decision-making node encounters an error.
    """
    pass


class ExecutionException(AgentException):
    """
    Raised when task execution fails.
    """
    pass


class ReflectionException(AgentException):
    """
    Raised when the reflection/self-check node fails.
    """
    pass


class DocumentGenerationException(AgentException):
    """
    Raised when the DOCX generation fails.
    """
    pass


class LLMException(AgentException):
    """
    Raised when communication with the LLM fails.
    """
    pass