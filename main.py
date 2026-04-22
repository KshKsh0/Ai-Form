import os
if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]
from fastapi import FastAPI, HTTPException
from schemas.dataSchema import promptStructer
from LLM.providers.OllamaProvider import OllamaProvider
from fastapi.middleware.cors import CORSMiddleware
import ollama



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your local HTML file to access the API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def status():
    return {'message ': 'hello world'}

@app.post('/generate')
async def generate_json(prompt:promptStructer):
    provider_name = prompt.provider.lower()
    
    if provider_name != 'ollama':
        raise HTTPException(status_code = 400 ,detail=f"Only 'ollama' provider is supported.")
        
    selected_provider = OllamaProvider(model_id=prompt.model)
    
     
    system_prompt = """
ACT AS A RAW DATA SERVER. OUTPUT ONLY VALID JSON. MUST NOT INCLUDE MARKDOWN FENCES (like ```json).
Schema: { "title": "string", "html": "string", "questions_count": "number" }

UI STYLE RULES:
1. Use FULL Tailwind CSS utility classes to create a premium, modern design.
2. Form background: apply glassmorphism using 'bg-white/80 backdrop-blur-xl shadow-2xl border border-white/40 rounded-3xl p-8'.
3. Layout: Use flexbox and grids ('flex flex-col gap-5', 'grid grid-cols-1 md:grid-cols-2 gap-4').
4. Inputs: 'w-full bg-gray-50 border-2 border-gray-100 focus:bg-white focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20 rounded-xl px-4 py-3 text-gray-700 transition-all duration-300'.
5. Buttons: 'w-full bg-gradient-to-r from-violet-600 to-indigo-600 hover:from-violet-700 hover:to-indigo-700 text-white font-bold py-3.5 rounded-xl shadow-lg hover:shadow-indigo-500/30 transition-all duration-300 transform hover:-translate-y-1'.
6. Typography: 'text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-indigo-600 mb-6' for titles, 'block text-sm font-semibold text-gray-700 mb-1' for labels.
7. Add proper placeholder texts. If possible, add inline SVG icons to labels or inputs.

DO NOT INCLUDE MARKDOWN FENCES. DO NOT EXPLAIN. ONLY RETURN PURE JSON.
"""
    output = await selected_provider.generate_json(
        system_prompt=system_prompt, 
        user_prompt=prompt.txt
    )
    return {
        'output': output,
        'meta': {
            'provider_used': prompt.provider,
            'model_used': prompt.model,
            'id': prompt.id
        }
    }
    
    
    
@app.get('/models')
async def list_models():
    try:
        # Use the global list() or AsyncClient().list()
        response = ollama.list()
        

        model_names = [m.model for m in response.models]
        
        return {"models": model_names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))