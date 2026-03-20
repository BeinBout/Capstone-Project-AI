from utils.ai.create_tool import create_tool
from utils.ai.tools.retrieve_information import retrieve_information
from schemas.llm_tool_calling import RetrieveInformationArgs

tools: list = [
    create_tool(retrieve_information.__name__, "For retrieve information from DB using RAG", RetrieveInformationArgs)
]