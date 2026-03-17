from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Recommendation(BaseModel):
    focus: str = Field(..., description="Focus area of the recommendation (e.g: 'Kualitas Tidur')")
    description: str = Field(..., description="Detailed description of the recommendation")


class AiInsights(BaseModel):
    risk_level: Literal["low", "moderate", "high", "severe"] = Field(
        ..., 
        description="Risk level string. MUST be exactly one of: 'low', 'moderate', 'high', 'severe'."
    )
    
    risk_score: int = Field(
        ..., 
        ge=0, 
        le=100, 
        description="Risk score integer ranging from 0 to 100 (e.g: 62)"
    )
    
    dominant_stressor: List[str] = Field(..., description="List of dominant stressors (e.g: ['academic_pressure', 'sleep_disorder'])")
    personality_summary: str = Field(..., description="Personality summary string (e.g: 'Kamu adalah tipe yang perfeksionis...')")
    
    recommendations: List[Recommendation] = Field(
        ..., 
        min_length=1,
        max_length=4,
        description="List of recommendation objects. Provide between 1 to 4 highly relevant recommendations."
    )
    
    progress_status: Optional[str] = Field(default=None, description="Progress status string (default: null)")
    weekly_insight: Optional[str] = Field(default=None, description="Weekly insight string (default: null)")
    ai_low_confidence: bool = Field(..., description="Whether AI confidence is low (e.g: false)")


class LLMInitialPersona(BaseModel):
    ai_summary: str = Field(..., description="AI summary string (e.g: 'Kamu cenderung memendam tekanan akademik...')")
    ai_insights: AiInsights = Field(..., description="Structured AI insights JSON object")
    
