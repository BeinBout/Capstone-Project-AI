from pydantic import BaseModel

def create_tool(name: str, description: str, schema_model: BaseModel) -> dict:
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": schema_model.model_json_schema(),
        }
    }