from typing import List
from app.utils.config import KENDRA_INDEX_ID
from app.utils.logger import logger

try:
    import boto3
except ImportError:  # fallback when boto3 is not installed
    boto3 = None


class KendraService:
    """Service wrapper for AWS Kendra queries.

    For portfolio/demo purposes, this implementation will:
    - if boto3 is available and properly configured, try to query Kendra
    - otherwise, return a mocked list of excerpts
    """

    def __init__(self):
        if boto3 is not None:
            try:
                self.kendra = boto3.client("kendra")
            except Exception as e:
                logger.warning(f"Could not initialize Kendra client: {e}")
                self.kendra = None
        else:
            self.kendra = None

    def query(self, text: str) -> List[str]:
        logger.info(f"Kendra query: {text}")

        if not self.kendra:
            # Mocked response for environments without AWS
            return [
                f"[MOCK] Relevant excerpt 1 for: {text}",
                f"[MOCK] Relevant excerpt 2 for: {text}",
            ]

        try:
            response = self.kendra.query(
                IndexId=KENDRA_INDEX_ID,
                QueryText=text,
                PageSize=3
            )
            excerpts = []
            for item in response.get("ResultItems", []):
                excerpt = item.get("DocumentExcerpt", {}).get("Text", "")
                if excerpt:
                    excerpts.append(excerpt)
            return excerpts
        except Exception as e:
            logger.error(f"Kendra query failed: {e}")
            return [f"[ERROR] Kendra query failed: {e}"]
