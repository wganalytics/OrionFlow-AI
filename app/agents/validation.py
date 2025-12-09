from app.utils.logger import logger


class ValidationAgent:
    """Agent responsible for applying basic validation and guardrails.

    In a real scenario this could:
    - enforce business rules
    - check forbidden terms
    - validate confidence thresholds
    - check regulatory constraints
    """

    def validate(self, reasoning: str) -> bool:
        if not reasoning or len(reasoning.strip()) == 0:
            logger.warning("Validation failed: empty reasoning.")
            return False

        # Very simple example rule: require a minimum length
        if len(reasoning) < 40:
            logger.warning("Validation failed: reasoning too short.")
            return False

        return True
