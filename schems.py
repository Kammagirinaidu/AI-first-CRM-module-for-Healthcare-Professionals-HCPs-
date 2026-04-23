from pydantic import BaseModel

class InteractionCreate(BaseModel):
    text: str