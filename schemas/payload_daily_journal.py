from pydantic import BaseModel
from typing import List


class UserContext(BaseModel):
    umur: int
    berat_badan: int
    tinggi_badan: int


class CurrentPersona(BaseModel):
    risk_level: str
    risk_score: str
    dominant_stressor: List[str]


class RecentTrend(BaseModel):
    last_3_days_avg_mood: float
    last_3_days_avg_sleep: float
    consecutive_negative_days: int


class Journal(BaseModel):
    mood: str
    mood_intensity: int
    sleep_duration_hours: float
    sleep_quality: str
    content: str


class DailyJournal(BaseModel):
    user_context: UserContext
    current_persona: CurrentPersona
    recent_trend: RecentTrend
    journal: Journal
