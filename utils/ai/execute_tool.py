import json
import inspect

from utils.ai.tools.retrieve_information import retrieve_information

TOOL_MAP = {
    retrieve_information.__name__: retrieve_information,
}

async def execute_tool(tool_call) -> dict:
    func_name = tool_call.function.name
    try:
        args_string = tool_call.function.arguments
        args = json.loads(args_string) if args_string else {}
    except json.JSONDecodeError:
        args = {}

    print(f"execute tool {func_name} with args: {args}")

    if func_name not in TOOL_MAP:
        print(f"function {func_name} not found in TOOL_MAP")
        result_data = {"error": f"Function {func_name} isnt available."}
    else:
        func_to_call = TOOL_MAP[func_name]
        
        try:
            if inspect.iscoroutinefunction(func_to_call):
                result_data = await func_to_call(**args)
            else:
                result_data = func_to_call(**args)
                
        except Exception as e:
            print(f"func exec failed for {func_name}: {e}")
            result_data = {"error": f"Failed to execute {func_name}: {str(e)}"}

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result_data, default=str),
    }