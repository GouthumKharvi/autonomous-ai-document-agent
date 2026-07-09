"""
LangGraph Workflow.

Builds and compiles the autonomous AI document workflow.
"""

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.graph.state import AgentState
from app.graph.memory import GraphMemory
from app.tools.logger import logger

from app.graph.nodes import (
    validation_node,
    planner_node,
    decision_node,
    executor_node,
    reflection_node,
    document_node,
    response_node,
)

from app.utils.constants import (
    VALIDATION_NODE,
    PLANNER_NODE,
    DECISION_NODE,
    EXECUTOR_NODE,
    REFLECTION_NODE,
    DOCUMENT_NODE,
    RESPONSE_NODE,
)


class AutonomousDocumentGraph:
    """
    Builds the LangGraph workflow.
    """

    def __init__(self) -> None:

        self.memory = GraphMemory()

        self.workflow = StateGraph(AgentState)

        self._build_graph()

        self.graph = self.workflow.compile(
            checkpointer=self.memory.checkpointer
        )

    def _build_graph(self) -> None:
        """
        Register all nodes and edges.
        """

        # ==================================================
        # Register Nodes
        # ==================================================

        self.workflow.add_node(
            VALIDATION_NODE,
            validation_node,
        )

        self.workflow.add_node(
            PLANNER_NODE,
            planner_node,
        )

        self.workflow.add_node(
            DECISION_NODE,
            decision_node,
        )

        self.workflow.add_node(
            EXECUTOR_NODE,
            executor_node,
        )

        self.workflow.add_node(
            REFLECTION_NODE,
            reflection_node,
        )

        self.workflow.add_node(
            DOCUMENT_NODE,
            document_node,
        )

        self.workflow.add_node(
            RESPONSE_NODE,
            response_node,
        )

        # ==================================================
        # Define Workflow
        # ==================================================

        self.workflow.add_edge(
            START,
            VALIDATION_NODE,
        )

        self.workflow.add_edge(
            VALIDATION_NODE,
            PLANNER_NODE,
        )

        self.workflow.add_edge(
            PLANNER_NODE,
            DECISION_NODE,
        )

        self.workflow.add_edge(
            DECISION_NODE,
            EXECUTOR_NODE,
        )

        self.workflow.add_edge(
            EXECUTOR_NODE,
            REFLECTION_NODE,
        )

        # ==================================================
        # Reflection Decision
        # ==================================================

        self.workflow.add_conditional_edges(
            REFLECTION_NODE,
            self._reflection_router,
            {
                "approved": DOCUMENT_NODE,
                "retry": EXECUTOR_NODE,
            },
        )

        self.workflow.add_edge(
            DOCUMENT_NODE,
            RESPONSE_NODE,
        )

        self.workflow.add_edge(
            RESPONSE_NODE,
            END,
        )

    def _reflection_router(
        self,
        state: AgentState,
    ):
        """
        Route the workflow after reflection.

        If approved -> Document

        If rejected -> Retry Executor

        Maximum retries = 2
        """

        if state["is_approved"]:

            logger.info(
                "Reflection approved the document."
            )

            return "approved"

        if state.get("retry_count", 0) >= 2:

            logger.warning(
                "Maximum retry limit reached. Proceeding with current document."
            )

            return "approved"

        logger.info(
            "Reflection rejected the document. Retrying Executor."
        )

        return "retry"

    def get_graph(self):
        """
        Return compiled graph.
        """

        return self.graph