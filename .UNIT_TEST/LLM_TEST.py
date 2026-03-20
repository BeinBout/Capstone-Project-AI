from pydantic import BaseModel

class TEST_SCHEMAS(BaseModel):
    reflection: str 
    metadata: dict