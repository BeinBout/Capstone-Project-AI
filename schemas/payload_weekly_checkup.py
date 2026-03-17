from pydantic import BaseModel
from typing import List


class UserContext(BaseModel):
    umur: int
    berat_badan: int
    tinggi_badan: int


class CurrentPersona(BaseModel):
    risk_level: str
    risk_score: int
    dominant_stressor: List[str]
    personality_summary: str


class WeeklyMetrics(BaseModel):
    avg_mood_intensity: float
    avg_sleep_hours: float
    dominant_mood: str
    negative_sentiment_ratio: float
    journal_entries_count: int
    anomaly_count: int


class CheckupAnswer(BaseModel):
    category: str
    question_text: str
    selected_option: str
    emotion_tag: str
    score_value: int


class WeeklyCheckup(BaseModel):
    user_context: UserContext
    current_persona: CurrentPersona
    weekly_metrics: WeeklyMetrics
    checkup_answers: List[CheckupAnswer]
    dominant_categories: List[str]
