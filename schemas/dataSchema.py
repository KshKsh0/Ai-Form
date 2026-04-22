from pydantic import BaseModel
from typing import Optional

class promptStructer(BaseModel):
    txt:str
    provider:str
    id: int
    model: Optional[str] = "minimax-m2.7:cloud"

    
    
