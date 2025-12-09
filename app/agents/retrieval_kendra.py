from typing import List
from app.services.kendra_service import KendraService


class RetrievalAgent:
    """Agent responsible for querying AWS Kendra (or mocked retrieval)."""

    def __init__(self):
        self.kendra = KendraService()

    def retrieve(self, query: str) -> List[str]:
        return self.kendra.query(query)
