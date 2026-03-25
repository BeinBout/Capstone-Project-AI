from openai import AsyncAzureOpenAI
from core.config import settings
from loguru import logger

client = AsyncAzureOpenAI(
    api_version=settings.AZURE_AI_API_VERSION,
    azure_endpoint=settings.AZURE_AI_ENDPOINT,
    api_key=settings.AZURE_AI_KEY_CREDENTIALS
)

async def embedding(input: str) -> dict:
    try:
        response = await client.embeddings.create(
            input=input,
            model=settings.AZURE_AI_EMBEDDING_DEPLOYMENT
        )
        
        return {
            "embedding": response.data[0].embedding,
            "usage": response.usage.total_tokens,
            "model": response.model
        }
    except Exception as e:
        logger.error(f"Azure AI API Error: \n {e}")
        raise e