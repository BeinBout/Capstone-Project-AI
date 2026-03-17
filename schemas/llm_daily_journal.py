from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

class LLMDailyJournal(BaseModel):
    ai_reflection: str = Field(
        ...,
        description=(
            "A warm, empathetic reflection written by the AI based on the user's journal entry. "
            "It should acknowledge the user's feelings and provide supportive insight. "
            'e.g: "Kamu sedang menghadapi tekanan yang cukup berat..."'
        ),
    )
    ai_tags: List[str] = Field(
        ...,
        description=(
            "A list of relevant tags extracted from the journal entry that categorize "
            "the main themes or issues mentioned by the user. "
            'e.g: ["academic_pressure", "sleep_deficit"]'
        ),
    )
    ai_sentiment_score: float = Field(
        ...,
        ge=-1.0,
        le=1.0,
        description=(
            "A sentiment score ranging from -1.0 (very negative) to 1.0 (very positive) "
            "representing the overall emotional tone of the journal entry. "
            "e.g: -0.72"
        ),
    )
    ai_anomaly_detected: bool = Field(
        ...,
        description=(
            "Indicates whether an anomaly or concerning pattern has been detected "
            "in the user's journal entry, such as signs of burnout, crisis, or extreme distress. "
            "e.g: true"
        ),
    )
    
    # PERUBAHAN DI SINI: Menggunakan Optional agar lebih aman dari LLM hallucination
    ai_anomaly_type: Optional[str] = Field(
        default=None, 
        description=(
            "Describes the type of anomaly detected, if any. Should be null or empty if "
            "no anomaly was detected. "
            'e.g: "sleep_deficit"'
        ),
    )
    ai_low_confidence: bool = Field(
        ...,
        description=(
            "Indicates whether the AI has low confidence in its analysis, "
            "typically due to vague, very short, or ambiguous journal content. "
            "e.g: false"
        ),
    )

    @model_validator(mode='after')
    def validate_anomaly_logic(self) -> 'LLMDailyJournal':
        if self.ai_anomaly_detected and not self.ai_anomaly_type:
            raise ValueError("ai_anomaly_type MUST be provided if ai_anomaly_detected is true.")
        
        if not self.ai_anomaly_detected and self.ai_anomaly_type:
            self.ai_anomaly_type = None
            
        return self