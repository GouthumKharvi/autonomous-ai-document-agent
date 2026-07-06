"""
LangGraph Memory.

Provides thread-based memory and checkpoint persistence
for the autonomous AI document agent.
"""

from langgraph.checkpoint.memory import MemorySaver


class GraphMemory:
    """
    Manages LangGraph memory and checkpoint persistence.
    """

    def __init__(self) -> None:
        self._checkpointer = MemorySaver()

    @property
    def checkpointer(self) -> MemorySaver:
        """
        Return the configured LangGraph checkpointer.
        """
        return self._checkpointer

    @staticmethod
    def get_config(thread_id: str) -> dict:
        """
        Create a LangGraph configuration for a conversation thread.

        Parameters
        ----------
        thread_id : str
            Unique identifier for the conversation.

        Returns
        -------
        dict
            LangGraph runtime configuration.
        """

        return {
            "configurable": {
                "thread_id": thread_id
            }
        }