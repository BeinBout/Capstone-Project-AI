from fastapi import Header, HTTPException
from core.config import settings

def req_validate(x_ai_api_call: str = Header(None)):
    if not x_ai_api_call or x_ai_api_call != settings.BEINBOUT_AI_CALL_KEY:
        raise HTTPException(status_code=403, detail="Request Forbidden!")
    return True