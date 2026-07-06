"""
Application logger configuration.
"""

import logging
from pathlib import Path

from app.utils.config import settings

# ==========================================================
# Create Logs Directory
# ==========================================================

Path(settings.LOG_DIR).mkdir(parents=True, exist_ok=True)

# ==========================================================
# Logger Configuration
# ==========================================================

LOG_FILE = Path(settings.LOG_DIR) / "agent.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("AutonomousAIAgent")