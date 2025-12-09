from app.agents.retrieval_kendra import RetrievalAgent
from app.agents.reasoning_bedrock import ReasoningAgent
from app.agents.validation import ValidationAgent
from app.agents.action import ActionAgent
from app.utils.logger import logger


class OrchestratorAgent:
    """Core orchestrator that coordinates all agents.

    Steps:
    1. Retrieve contextual information from Kendra
    2. Run LLM reasoning on the retrieved context
    3. Validate reasoning according to simple guardrails
    4. Optionally trigger external action via ActionAgent
    """

    def __init__(self):
        self.retrieval = RetrievalAgent()
        self.reasoning = ReasoningAgent()
        self.validation = ValidationAgent()
        self.action = ActionAgent()

    async def run(self, query: str, execute_action: bool):
        logger.info("Starting OrionFlow multi-agent workflow...")

        # 1) Retrieval
        retrieved_docs = self.retrieval.retrieve(query)
        combined_context = "\n---\n".join(retrieved_docs) if retrieved_docs else query

        # 2) Reasoning
        reasoning_output = self.reasoning.think(combined_context)

        # 3) Validation
        if not self.validation.validate(reasoning_output):
            return {
                "error": "Validation failed",
                "reasoning": reasoning_output,
                "retrieved_docs": retrieved_docs,
            }

        result = {
            "reasoning": reasoning_output,
            "retrieved_docs": retrieved_docs,
        }

        # 4) Optional action
        if execute_action:
            action_payload = {
                "query": query,
                "reasoning": reasoning_output
            }
            action_result = self.action.execute(action_payload)
            result["action"] = action_result

        return result
