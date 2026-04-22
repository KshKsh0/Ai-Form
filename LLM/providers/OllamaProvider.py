import ollama 
import json 
from ..LLMInterface import LLMInterface
import re

#ollama support async so it huge advantige for us ! 

class OllamaProvider(LLMInterface):
    
    def __init__(self, model_id :str ) :
        self.model_id = model_id
        self.client = ollama.AsyncClient()
        
    async def generate_json(self, system_prompt: str, user_prompt: str):
        try:
            res = await self.client.chat(
                model=self.model_id,
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': user_prompt},
                ],
                format='json'
            )
            
            content = res['message']['content'].strip()

            # 2. THE FIX: Use Regex to find the JSON block
            # This looks for the first '{' and the last '}'
            match = re.search(r'\{.*\}', content, re.DOTALL)
            
            if match:
                json_str = match.group()
                return json.loads(json_str)
            else:
                # If no braces found, return the raw content for debugging
                print(f"DEBUG: No JSON found in: {content}")
                return {"error": "No JSON found", "raw": content}
                
        except json.JSONDecodeError as e:
            print(f"JSON Error: {e} | Content: {content}")
            return {"error": "Invalid JSON syntax from model"}
        except Exception as e:
            return {"error": str(e)}
                
    async def pull_model(self, model_id: str):
        """Downloads a model from the Ollama library."""
        return await self.client.pull(model=model_id)

    async def delete_model(self, model_id: str):
        """Removes a model from your local machine to save space."""
        return await self.client.delete(model=model_id)

    async def push_model(self, model_id: str):
        """Uploads a custom model to your Ollama library/registry."""
        return await self.client.push(model=model_id)