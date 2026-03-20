from fastapi import APIRouter
from core.ai.llm_agent import chat_agent
from utils.ai.tool import tools
from schemas.llm_weekly_checkup import LLMWeeklyCheckup, SYSTEM_PROMPT_CHECKUP
from schemas.payload_weekly_checkup import WeeklyCheckup
import json

router = APIRouter(tags=["Weekly Checkup"])

@router.post('/weekly_checkup')
async def daily_journal(payload: WeeklyCheckup):
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT_CHECKUP},
        {"role": "user", "content": f"{json.dumps(payload.model_dump(), indent=2)}"}
    ]
    
    return await chat_agent(messages, tools, LLMWeeklyCheckup)