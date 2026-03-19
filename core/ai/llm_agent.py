from openai import OpenAI
from utils.ai.execute_tool import execute_tool

CLIENT = OpenAI(
    api_key="sk-46d8acc7458d4d63b36e4e05c7eacbd2",
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)
MODEL = "qwen3.5-plus"

async def chat_agent(messages: list, tools: list):
    while True:
        print("thinking...")
        response = CLIENT.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        agent_message = response.choices[0].message
        messages.append(agent_message)
        
        if agent_message.tool_calls is None:
            print(f"\nFinal Result:\n{agent_message.content}")
            break 
            
        for tool_call in agent_message.tool_calls:
            print(f"exec tool: {tool_call.function.name}")
            tool_message = await execute_tool(tool_call)
            
            print(f"Tool {tool_call.function.name} return : {tool_message['content'][:100]}...") 
            messages.append(tool_message)