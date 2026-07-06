"""
Application-wide constants.

Avoid hardcoding strings throughout the project.
Import constants from this file whenever possible.
"""

# ==========================================================
# Application
# ==========================================================

APP_NAME = "Autonomous AI Document Agent"

APP_VERSION = "1.0.0"

# ==========================================================
# Supported LLM Providers
# ==========================================================

GEMINI = "gemini"
OPENAI = "openai"

SUPPORTED_MODEL_PROVIDERS = [
    GEMINI,
    OPENAI,
]

# ==========================================================
# Supported Document Types
# ==========================================================

DOCUMENT_TYPES = [
    "Business Proposal",
    "Meeting Minutes",
    "Project Plan",
    "Business Report",
    "Technical Design",
    "Standard Operating Procedure",
    "Product Specification",
]

# ==========================================================
# LangGraph Node Names
# ==========================================================

VALIDATION_NODE = "validation"

PLANNER_NODE = "planner"

DECISION_NODE = "decision"

EXECUTOR_NODE = "executor"

REFLECTION_NODE = "reflection"

DOCUMENT_NODE = "document"

RESPONSE_NODE = "response"

# ==========================================================
# Default Assumptions
# ==========================================================

DEFAULT_BUDGET = "₹25 Lakhs"

DEFAULT_TIMELINE = "6 Months"

DEFAULT_TEAM_SIZE = "6 Members"

DEFAULT_COMPANY_NAME = "ABC Technologies Pvt. Ltd."

# ==========================================================
# Default Output File
# ==========================================================

DEFAULT_OUTPUT_FILENAME = "generated_document.docx"