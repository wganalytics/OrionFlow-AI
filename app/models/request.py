from pydantic import BaseModel

class OrionRequest(BaseModel):
    user_query: str
    execute_action: bool = False
