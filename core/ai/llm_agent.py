from openai import AzureOpenAI
from openai.types.chat import ChatCompletionMessageToolCall
from typing import Type, cast
from pydantic import BaseModel, ValidationError
from loguru import logger
from core.config import settings

from utils.ai.execute_tool import execute_tool

CLIENT = AzureOpenAI(
    api_version=settings.AZURE_AI_API_VERSION,
    azure_endpoint=settings.AZURE_AI_ENDPOINT,
    api_key=settings.AZURE_AI_KEY_CREDENTIALS,
)
MODEL = settings.AZURE_AI_LLM_MODEL_NAME

async def chat_agent(messages: list, tools: list, structured_output: Type[BaseModel]):
    while True:
        logger.info("thinking...")
        response = CLIENT.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        agent_message = response.choices[0].message
        messages.append(agent_message)

        if not agent_message.tool_calls:
            logger.info("thinking done")
            break

        for R_tool_call in agent_message.tool_calls:
            tool_call = cast(ChatCompletionMessageToolCall, R_tool_call)
            logger.debug(f"exec tool: {tool_call.function.name}")
            tool_message = await execute_tool(tool_call)

            logger.debug(
                f"Tool {tool_call.function.name} return : {tool_message['content'][:100]}..."
            )
            messages.append(tool_message)
            
    logger.info("making final result...")
    
    final_response = CLIENT.beta.chat.completions.parse(
        model=MODEL,
        messages=messages,
        response_format=structured_output
    )
    
    final_result = final_response.choices[0].message.parsed
    
    if final_result is None:
        raise ValueError("LLM returned no content to parse")
        
    return final_result.model_dump()