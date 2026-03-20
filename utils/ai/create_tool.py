from pydantic import BaseModel
from typing import Type

def create_tool(name: str, description: str, schema_model: Type[BaseModel]) -> dict:
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": schema_model.model_json_schema(),
        }
    }