from app.services.openai_client import analyze_with_openai
from app.services.claud_client import analyze_with_claude


def analyze_email(text: str, model: str = "openai") -> dict:
    if model == "openai":
        return analyze_with_openai(text)
    elif model == "claude":
        return analyze_with_claude(text)
    else:
        raise ValueError(f"Unknown model: {model}")
