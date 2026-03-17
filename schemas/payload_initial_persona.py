from pydantic import BaseModel, Field

class UserContext(BaseModel):
    umur: int = Field(..., ge=0, le=120) 
    berat_badan: int = Field(..., gt=0)
    tinggi_badan: int = Field(..., gt=0)
    bmi_calc: float = Field(..., gt=0)

class Answer(BaseModel):
    category: str
    question_text: str
    selected_option: str
    emotion_tag: str
    score_value: int

class InitialPersona(BaseModel):
    user_context: UserContext
    answers: list[Answer]
    total_score: int
    dominant_categories: list[str]
