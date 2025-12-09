from app.services.integrations import IntegrationsService
from app.utils.logger import logger


class ActionAgent:
    """Agent responsible for triggering external system actions."""

    def __init__(self):
        self.integrations = IntegrationsService()

    def execute(self, payload: dict):
        logger.info("Executing action via IntegrationsService...")
        status, result = self.integrations.call_default_action(payload)
        return {
            "status_code": status,
            "response": result
        }
