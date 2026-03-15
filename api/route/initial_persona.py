from fastapi import APIRouter

router = APIRouter(tags=["Initial Persona"])

@router.post('/initial_persona')
async def initial_persona(body = "should be pydantic"):
    return "should be json output"