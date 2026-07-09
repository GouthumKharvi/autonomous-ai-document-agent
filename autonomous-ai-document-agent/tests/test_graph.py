"""
Tests for the LangGraph workflow.
"""

from app.graph.graph import AutonomousDocumentGraph


def test_graph_creation():
    """
    Verify the LangGraph object is created successfully.
    """

    graph = AutonomousDocumentGraph()

    assert graph is not None


def test_graph_compiles():
    """
    Verify the workflow compiles successfully.
    """

    workflow = AutonomousDocumentGraph()

    assert workflow.get_graph() is not None


def test_graph_has_memory():
    """
    Verify graph memory/checkpointer is initialized.
    """

    workflow = AutonomousDocumentGraph()

    assert workflow.memory is not None


def test_graph_instance():
    """
    Verify the compiled graph instance exists.
    """

    workflow = AutonomousDocumentGraph()

    graph = workflow.get_graph()

    assert graph is not None