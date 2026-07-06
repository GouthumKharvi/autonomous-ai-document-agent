from pathlib import Path

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Settings:
    """
    Central configuration for the entire application.
    """

    # ==========================================================
    # PROJECT PATHS
    # ==========================================================

    BASE_DIR = Path(__file__).resolve().parents[2]

    OUTPUT_DIR = BASE_DIR / "outputs"

    LOG_DIR = BASE_DIR / "logs"

    CHECKPOINT_DIR = BASE_DIR / "checkpoints"

    # ==========================================================
    # API KEYS
    # ==========================================================

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # ==========================================================
    # MODEL CONFIGURATION
    # ==========================================================

    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "gemini")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gemini-2.5-flash"
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", 0.2)
    )

    MAX_TOKENS = int(
        os.getenv("MAX_TOKENS", 4096)
    )

    # ==========================================================
    # APPLICATION SETTINGS
    # ==========================================================

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    APP_NAME = "Autonomous AI Document Agent"

    API_VERSION = "v1"


settings = Settings()