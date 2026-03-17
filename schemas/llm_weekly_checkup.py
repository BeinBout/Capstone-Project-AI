from pydantic import BaseModel, Field
from typing import List

class UserContext(BaseModel):
    umur: int = Field(..., gt=0)
    berat_badan: int = Field(..., gt=0)
    tinggi_badan: int = Field(..., gt=0)

class CurrentPersona(BaseModel):
    risk_level: str
    risk_score: int
    dominant_stressor: List[str]
    personality_summary: str

class WeeklyMetrics(BaseModel):
    avg_mood_intensity: float
    avg_sleep_hours: float = Field(..., ge=0, le=24.0) 
    dominant_mood: str
    negative_sentiment_ratio: float = Field(..., ge=-1.0, le=1.0) 
    journal_entries_count: int = Field(..., ge=0)
    anomaly_count: int = Field(..., ge=0)

class CheckupAnswer(BaseModel):
    category: str
    question_text: str
    selected_option: str
    emotion_tag: str
    score_value: int = Field(..., ge=0)

class WeeklyCheckup(BaseModel):
    user_context: UserContext
    current_persona: CurrentPersona
    weekly_metrics: WeeklyMetrics
    checkup_answers: List[CheckupAnswer]
    dominant_categories: List[str]