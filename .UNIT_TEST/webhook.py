import httpx
from core.ai.llm_agent import chat_agent
from core.config import settings

async def agent_webhook(messages: list[dict], tools: list, webhook_url: str = settings.WEBHOOK_URL):
    result = await chat_agent(messages, tools)
    
    payload: dict = {
        "status": "success",
        "data": {
            "ai_response": result
        }
    }
    
    print("Sending to webhook....")
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post(webhook_url, json=payload)
            print(f"Webhook send success: {res.status_code}")
        except Exception as e:
            print(f"Webhook send err: {e}")