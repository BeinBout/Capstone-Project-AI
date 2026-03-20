from fastapi import APIRouter
from schemas.payload_initial_persona import InitialPersona
from schemas.llm_initial_persona import SYSTEM_PROMPT_INITIAL_PERSONA, LLMInitialPersona
from core.ai.llm_agent import chat_agent
from utils.ai.tool import tools

import json

router = APIRouter(tags=["Initial Persona"])

@router.post('/initial_persona')
async def initial_persona(payload: InitialPersona):
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT_INITIAL_PERSONA},
        {"role": "user", "content": f"{json.dumps(payload.model_dump(), indent=2)}"}
    ]
    
    return await chat_agent(messages, tools, LLMInitialPersona)