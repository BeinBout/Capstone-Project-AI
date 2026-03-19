from pydantic import BaseModel, Field

class LocationArgs(BaseModel):
    location: str = Field(..., description="The name of the city")

class EmbeddingArgs(BaseModel):
    input: str = Field(..., description="Text to embed")
    
class RetrieveInformationArgs(BaseModel):
    input: str = Field(..., description="Text or query to search for RAG")