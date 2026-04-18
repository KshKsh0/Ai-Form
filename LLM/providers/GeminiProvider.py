from typing import Any, Dict

from ..LLMInterface import LLMInterface
import json
import google.generativeai as genai

class GeminiProvider(LLMInterface):
    
    def __init__(self , api_key :str ,model_id :str = 'gemini-2.5-flash'):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_id)
        
    async def generate_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        full_prompt = f"{system_prompt}\n\nUser Input: {user_prompt}"
        response = self.model.generate_content(
            full_prompt,
            generation_config={"response_mime_type": "application/json"} # option to make llm preduce json files 
        )
        return json.loads(response.text)
        