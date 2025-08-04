import os
import httpx
from dotenv import load_dotenv

load_dotenv()

async def analyze(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.4,
        "top_p": 0.9
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.together.xyz/v1/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()["choices"][0]["text"].strip()
