import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "autonomous-ai-document-agent"

list_of_files = [
    # app root
    "app/__init__.py",
    "app/main.py",

    # api
    "app/api/__init__.py",
    "app/api/routes.py",

    # graph
    "app/graph/__init__.py",
    "app/graph/graph.py",
    "app/graph/state.py",
    "app/graph/nodes.py",
    "app/graph/memory.py",

    # agents
    "app/agents/__init__.py",
    "app/agents/planner.py",
    "app/agents/decision.py",
    "app/agents/executor.py",
    "app/agents/reflection.py",
    "app/agents/response.py",

    # services
    "app/services/__init__.py",
    "app/services/gemini_service.py",
    "app/services/prompt_builder.py",
    "app/services/assumption_service.py",
    "app/services/document_service.py",

    # tools
    "app/tools/__init__.py",
    "app/tools/docx_tool.py",
    "app/tools/mock_data_tool.py",
    "app/tools/validation_tool.py",
    "app/tools/logger.py",

    # models
    "app/models/__init__.py",
    "app/models/request.py",
    "app/models/response.py",
    "app/models/agent_state.py",

    # utils
    "app/utils/__init__.py",
    "app/utils/constants.py",
    "app/utils/config.py",
    "app/utils/helpers.py",
    "app/utils/exceptions.py",

    # prompts
    "app/prompts/__init__.py",
    "app/prompts/planner_prompt.py",
    "app/prompts/reflection_prompt.py",
    "app/prompts/document_prompt.py",

    # top-level data/output dirs (with .gitkeep so empty dirs are tracked)
    "checkpoints/.gitkeep",
    "outputs/.gitkeep",
    "logs/.gitkeep",

    # tests
    "tests/__init__.py",
    "tests/test_api.py",
    "tests/test_graph.py",
    "tests/test_agent.py",
    "tests/test_tools.py",

    # root files
    ".env",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "LICENSE",
]


def create_project_structure(base_dir: str = ".") -> None:
    """
    Creates the full folder/file scaffold for the project.
    Safe to re-run: existing non-empty files are left untouched,
    missing directories/files are created.
    """
    base_path = Path(base_dir) / project_name

    for file_path in list_of_files:
        full_path = base_path / file_path
        directory = full_path.parent

        if directory != Path("") and not directory.exists():
            os.makedirs(directory, exist_ok=True)
            logging.info(f"Created directory: {directory}")

        if (not full_path.exists()) or (full_path.stat().st_size == 0):
            with open(full_path, "w") as f:
                pass
            logging.info(f"Created empty file: {full_path}")
        else:
            logging.info(f"File already exists and is non-empty, skipping: {full_path}")


if __name__ == "__main__":
    create_project_structure()
    logging.info(f"Project structure for '{project_name}' generated successfully.")
