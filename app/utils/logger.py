import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - ORIONFLOW - %(levelname)s - %(message)s"
)

logger = logging.getLogger("orionflow")
