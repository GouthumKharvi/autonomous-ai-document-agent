"""
LangGraph Nodes.

Defines every node executed inside the autonomous workflow.
"""

from app.agents.planner import PlannerAgent
from app.agents.decision import DecisionAgent
from app.agents.executor import ExecutorAgent
from app.agents.reflection import ReflectionAgent
from app.services.document_service import DocumentService
from app.graph.state import AgentState
from app.tools.logger import logger


planner = PlannerAgent()
decision = DecisionAgent()
executor = ExecutorAgent()
reflection = ReflectionAgent()
document_service = DocumentService()


# ==========================================================
# Validation Node
# ==========================================================

def validation_node(state: AgentState) -> AgentState:
    """
    Validate the incoming request.

    ValidationTool will be integrated later.
    """

    logger.info("Validation Node Started.")

    logger.info("Validation Node Completed.")

    return state


# ==========================================================
# Planner Node
# ==========================================================

def planner_node(state: AgentState) -> AgentState:
    """
    Execute Planner Agent.
    """

    logger.info("Planner Node Started.")

    execution_plan = planner.execute(
        request=state["request"]
    )

    state["execution_plan"] = execution_plan

    logger.info("Planner Node Completed.")

    return state


# ==========================================================
# Decision Node
# ==========================================================

def decision_node(state: AgentState) -> AgentState:
    """
    Execute Decision Agent.
    """

    logger.info("Decision Node Started.")

    document_type, assumptions = decision.execute(
        request=state["request"],
        execution_plan=state["execution_plan"],
    )

    state["document_type"] = document_type
    state["assumptions"] = assumptions

    logger.info("Decision Node Completed.")

    return state


# ==========================================================
# Executor Node
# ==========================================================

def executor_node(state: AgentState) -> AgentState:
    """
    Execute Executor Agent.
    """

    logger.info("Executor Node Started.")

    generated_content = executor.execute(
        request=state["request"],
        document_type=state["document_type"],
        assumptions=state["assumptions"],
    )

    state["generated_content"] = generated_content

    logger.info("Executor Node Completed.")

    return state


# ==========================================================
# Reflection Node
# ==========================================================

def reflection_node(state: AgentState) -> AgentState:
    """
    Execute Reflection Agent.
    """

    logger.info("Reflection Node Started.")

    approved, feedback = reflection.execute(
        generated_content=state["generated_content"]
    )

    state["approved"] = approved
    state["reflection_feedback"] = feedback

    logger.info("Reflection Node Completed.")

    return state


# ==========================================================
# Document Node
# ==========================================================

def document_node(state: AgentState) -> AgentState:
    """
    Generate the final Microsoft Word document.
    """

    logger.info("Document Node Started.")

    output_file = document_service.create_document(
        document_type=state["document_type"],
        generated_content=state["generated_content"],
    )

    state["output_file"] = output_file

    logger.info("Document Node Completed.")

    return state


# ==========================================================
# Response Node
# ==========================================================

def response_node(state: AgentState) -> AgentState:
    """
    Final workflow node.

    Returns the updated workflow state.
    """

    logger.info("Response Node Started.")

    logger.info("Workflow Completed Successfully.")

    return state