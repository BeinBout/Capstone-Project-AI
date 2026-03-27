from pydantic import BaseModel, Field

class EmbeddingArgs(BaseModel):
    input: str = Field(..., description="Text to embed")
    
class RetrieveInformationArgs(BaseModel):
    input: str = Field(..., description="Text or query to search for RAG")
    source_type: str | None = Field(description="Source type for search data at DB. The Enumerate: counsel_chat | emotion | genz_mental_wellness_and_digital_lifestyle | Mental_Health_Conversational_Data | mental_health_counseling | osmi_tech_2016 | reddit_community | reddit_mental_health_classific | sleep_health_and_lifestyle | student_mental_health. It's Optional, unless you need specific source from.")