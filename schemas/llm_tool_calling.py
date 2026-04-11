from pydantic import BaseModel, Field
from typing import Optional, Literal

class EmbeddingArgs(BaseModel):
    input: str = Field(..., description="Text to embed")
    
class RetrieveInformationArgs(BaseModel):
    input: str = Field(
        ..., 
        description="English query text to search psychological knowledge base."
    )
    source_type: Optional[Literal[
        "counsel_chat",
        "emotion",
        "genz_mental_wellness_and_digital_lifestyle",
        "Mental_Health_Conversational_Data",
        "mental_health_counseling",
        "osmi_tech_2016",
        "reddit_community",
        "reddit_mental_health_classific",
        "sleep_health_and_lifestyle",
        "student_mental_health"
    ]] = Field(
        default=None,
        description="""Filter search to a specific dataset. Leave null to search all sources.
Choose based on query focus:
- counsel_chat: therapist-client dialogue, coping strategies, emotional support responses
- emotion: emotion classification and detection patterns
- genz_mental_wellness_and_digital_lifestyle: Gen Z digital habits, social media impact, online stress
- Mental_Health_Conversational_Data: general mental health Q&A and conversations
- mental_health_counseling: structured counseling sessions, therapeutic techniques
- osmi_tech_2016: mental health in tech/workplace context, professional burnout
- reddit_community: peer support discussions, real user experiences with mental health
- reddit_mental_health_classific: classified mental health posts (depression, anxiety, etc.)
- sleep_health_and_lifestyle: sleep patterns, sleep disorders, lifestyle impact on sleep
- student_mental_health: academic pressure, student burnout, campus mental health"""
    )