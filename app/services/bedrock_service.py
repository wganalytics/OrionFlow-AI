from app.utils.logger import logger

try:
    import boto3
except ImportError:
    boto3 = None


class BedrockService:
    """Service wrapper for AWS Bedrock LLM.

    For portfolio/demo purposes, this implementation:
    - logs the prompt
    - returns a mocked reasoning string
    - real Bedrock integration can be plugged following AWS docs
    """

    def __init__(self):
        if boto3 is not None:
            try:
                self.client = boto3.client("bedrock-runtime")
            except Exception as e:
                logger.warning(f"Could not initialize Bedrock client: {e}")
                self.client = None
        else:
            self.client = None

    def reason(self, prompt: str) -> str:
        logger.info("Generating LLM reasoning (mock/Bedrock)...")

        # For now, we keep a safe mock that always works,
        # avoiding runtime errors in environments without AWS.
        return (
            "[LLM REASONING MOCK]\n"
            "Prompt received (truncated):\n" +
            (prompt[:400] + ("..." if len(prompt) > 400 else ""))
        )
