from app.config.providers import PROVIDERS
import re

async def analyze_email(email: str, provider: str) -> dict:
    prompt = f"""
    Analyze the following email from an important client and gather sentiment provide the feedback:
    Tone (choose one): [Angry, Polite, Grateful, Neutral, Urgent]
    Urgency: 1 (low) to 5 (high)
    Suggested Action: [Escalate, Respond, Ignore, Follow-up]
    Sentiment: [Positive, Negative, Neutral, Mixed, Unclear]
    Email: "{email}"
    Return this JSON structure: {{"tone": "...", "sentiment": "...", "urgency": <1-5>, "suggestedAction": "..."}}
    """
    analyze = PROVIDERS.get(provider)
    if not analyze:
        raise ValueError(f"Unknown provider: {provider}")
    result = await analyze(prompt)
    sentiment = re.search(r"sentiment\s*=\s*[\"'](\w+)[\"']", result, re.IGNORECASE)
    tone = re.search(r"tone\s*=\s*[\"'](\w+)[\"']", result, re.IGNORECASE)
    urgency = re.search(r"urgency\s*=\s*(\d)", result, re.IGNORECASE)
    suggested_action = re.search(r"suggestedAction\s*=\s*[\"'](\w+)[\"']", result, re.IGNORECASE)
    form_result =      {
        "sentiment": sentiment.group(1) if sentiment else None,
        "tone": tone.group(1) if tone else None,
        "urgency": int(urgency.group(1)) if urgency else None,
        "suggested_action": suggested_action.group(1) if suggested_action else None
    }
    return {"result": form_result}
