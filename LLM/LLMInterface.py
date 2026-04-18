from abc import ABC, abstractmethod
from typing import Any, Dict

class LLMInterface(ABC):
    
    @abstractmethod
    def __init__(self, api_key: str, model_id: str):
        """Initialize the client with credentials and model choice."""
        pass

    @abstractmethod
    async def generate_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """
        Sends a request to the LLM and forces a JSON response.
        We make it 'async' so it doesn't block your FastAPI server.
        """
        pass