from typing import Tuple
import requests
from app.utils.config import ACTION_WEBHOOK_URL
from app.utils.logger import logger


class IntegrationsService:
    """Generic HTTP integration layer for external systems.

    In a real scenario, this could call:
    - Jira
    - ERP
    - CRM
    - Ticketing systems
    - Custom webhooks
    """

    def call_system(self, url: str, payload: dict) -> Tuple[int, str]:
        logger.info(f"Executing external action: {url}")
        try:
            response = requests.post(url, json=payload, timeout=10)
            return response.status_code, response.text
        except Exception as e:
            logger.error(f"Error calling external system: {e}")
            return 500, str(e)

    def call_default_action(self, payload: dict) -> Tuple[int, str]:
        """Convenience wrapper using default ACTION_WEBHOOK_URL."""
        return self.call_system(ACTION_WEBHOOK_URL, payload)
