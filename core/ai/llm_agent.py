from openai import OpenAI
from openai.types.chat import ChatCompletionMessageToolCall
from typing import Type, cast
from pydantic import BaseModel, ValidationError
from loguru import logger

from utils.ai.execute_tool import execute_tool

CLIENT = OpenAI(
    api_key="sk-46d8acc7458d4d63b36e4e05c7eacbd2",
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
MODEL = "qwen3.5-plus"


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
    
    final_response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=messages,
        response_format={"type": "json_object"}
    )
    
    final_result = final_response.choices[0].message.content
    
    if final_result is None:
        raise ValueError("LLM returned no content to parse")
        
    try:
        parsed_pydantic = structured_output.model_validate_json(final_result)
        return parsed_pydantic.model_dump()
        
    except ValidationError as e:
        
        logger.error(f"Pydantic LLM err: {e}")