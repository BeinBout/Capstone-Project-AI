from fastapi import APIRouter
from core.ai.llm_agent import chat_agent
from utils.ai.tool import tools
from schemas.llm_daily_journal import LLMDailyJournal, SYSTEM_PROMPT_DAILY_JOURNAL
from schemas.payload_daily_journal import DailyJournal
import json

router = APIRouter(tags=["Daily Journal"])

@router.post('/daily_journal')
async def daily_journal(payload: DailyJournal):
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT_DAILY_JOURNAL},
        {"role": "user", "content": f"{json.dumps(payload.model_dump(), indent=2)}"}
    ]
    
    return await chat_agent(messages, tools, LLMDailyJournal)