# app/services/sentiment.py
from app.config.llm_clients.llm_client import chat
import json, re

SYSTEM = {
    "role": "system",
    "content": "You analyze email tone and return a JSON with tone, confidence, and notes.",
}


async def analyze_email(subject: str, body: str):
    user = {
        "role": "user",
        "content": f"""Analyze the following email from an important client and gather sentiment:

Tone (choose one): [Angry, Polite, Grateful, Neutral, Urgent]
Urgency: 1 (low) to 5 (high)
Suggested Action: [Escalate, Respond, Ignore, Follow-up]
Sentiment: [Positive, Negative, Neutral, Mixed, Unclear]

Subject: "{subject}"
Email: "{body}"

Return ONLY this JSON structure (no prose): {{"tone": "...", "sentiment": "...", "urgency": <1-5>, "suggestedAction": "..."}}""",
    }

    raw = await chat([SYSTEM, user])
    data = None
    try:
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if m:
            data = json.loads(m.group(0))
        else:
            data = json.loads(raw)
    except Exception:
        sentiment = re.search(r'"?sentiment"?\s*[:=]\s*"?(\w+)"?', raw, re.I)
        tone = re.search(r'"?tone"?\s*[:=]\s*"?(\w+)"?', raw, re.I)
        urgency = re.search(r'"?urgency"?\s*[:=]\s*(\d)', raw, re.I)
        action = re.search(r'"?suggestedAction"?\s*[:=]\s*"?([\w\- ]+)"?', raw, re.I)
        data = {
            "sentiment": sentiment.group(1) if sentiment else None,
            "tone": tone.group(1) if tone else None,
            "urgency": int(urgency.group(1)) if urgency else None,
            "suggestedAction": action.group(1) if action else None,
        }

    return {"result": data}
