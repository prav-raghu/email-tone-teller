# app/config/llm_clients/llm_client.py
import os, httpx
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY is missing.")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": os.getenv("APP_URL", ""),
    "X-Title": os.getenv("APP_NAME", ""),
    "Content-Type": "application/json",
}


async def chat(messages, model=None, **opts):
    model = model or os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    payload = {"model": model, "messages": messages}
    if "temperature" in opts:
        payload["temperature"] = opts["temperature"]
    if "max_tokens" in opts:
        payload["max_tokens"] = opts["max_tokens"]

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(BASE_URL, headers=HEADERS, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
