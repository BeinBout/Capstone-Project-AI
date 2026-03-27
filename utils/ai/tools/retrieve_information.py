from core.ai.embed import embedding
from utils.rag_search import rag_search

async def retrieve_information(input: str, source_type: str | None = None) -> list[dict]:
    vector = await embedding(input)
    results = await rag_search(vector['embedding'], source_type=source_type)
    
    return [
        {
            **{
                k: v
                for k, v in row.__dict__.items()
                if k != 'embedding' and not k.startswith('_')
            },
            'distance': distance
        }
        for row, distance in results
    ]