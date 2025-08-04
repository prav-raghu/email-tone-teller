from app.config.llm_clients.openai_client import analyze as openai
from app.config.llm_clients.claud_client import analyze as claude
from app.config.llm_clients.llma_client import analyze as llama

PROVIDERS = {"openai": openai, "claude": claude, "llama": llama}
