from fastapi import APIRouter
from schemas.payload_initial_persona import InitialPersona
import json

router = APIRouter(tags=["Initial Persona"])

@router.post('/initial_persona')
async def initial_persona(body: InitialPersona):
    return json.dumps(body.model_json_schema(), indent=2)