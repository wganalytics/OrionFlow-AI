from app.services.bedrock_service import BedrockService


class ReasoningAgent:
    """Agent responsible for LLM-based reasoning using Bedrock (mocked)."""

    def __init__(self):
        self.llm = BedrockService()

    def think(self, context: str) -> str:
        prompt = (
            "You are an AI assistant orchestrator inside OrionFlow AI.\n"
            "Analyze the following context and produce structured insights,\n"
            "including key risks, opportunities and next best actions.\n\n"
            f"Context:\n{context}\n\n"
            "Return a concise, bullet-point style summary.\n"
        )
        return self.llm.reason(prompt)
