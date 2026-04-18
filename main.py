from fastapi import FastAPI
from schemas.dataSchema import promptStructer
from LLM.providers.GeminiProvider import GeminiProvider
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your local HTML file to access the API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_client = GeminiProvider(api_key="AIzaSyCoJZVFAJf1tE5uBm58Fu6pEcJfrN-38rI")

@app.get('/')
async def status():
    return {'message ': 'hello world'}


@app.post('/generate')
async def generate_json(prompt: promptStructer):
    user_input = prompt.txt  
    final_llm_prompt = f"""
    System: You are a UI generator that outputs raw JSON.
    
    JSON Schema to follow:
    {{
        "title": "string",
        "html": "string (the HTML form)",
        "questions_count": "number"
    }}
    """
    
    output = await llm_client.generate_json(system_prompt = final_llm_prompt , user_prompt = user_input )
    
    
    return {'output':output }