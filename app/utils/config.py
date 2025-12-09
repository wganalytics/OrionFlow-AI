import os

# Basic configuration and environment variables

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
KENDRA_INDEX_ID = os.getenv("KENDRA_INDEX_ID", "YOUR_KENDRA_INDEX_ID")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-v2")
ACTION_WEBHOOK_URL = os.getenv("ACTION_WEBHOOK_URL", "https://example.com/api/action")
