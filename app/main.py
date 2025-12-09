from fastapi import FastAPI
from app.models.request import OrionRequest
from app.agents.orchestrator import OrchestratorAgent

app = FastAPI(
    title="OrionFlow AI",
    description="Multi-Agent Orchestration Engine with AWS Bedrock + Kendra + Kestra",
    version="1.0.0"
)

orchestrator = OrchestratorAgent()

@app.post("/orionflow/run")
async def run_orionflow(request: OrionRequest):
    """Main endpoint that triggers the multi-agent orchestration flow."""
    result = await orchestrator.run(request.user_query, request.execute_action)
    return {"result": result}
