import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_with_openai(email_text: str):
    prompt = f"""
You are a helpful assistant. Analyze the following client email and extract:
1. The tone (e.g., friendly, annoyed, neutral, passive-aggressive)
2. The urgency level (low, medium, high)
3. A professional reply to send back
4. A short summary of what the client is asking for

Respond in a JSON format like:
{{
  "tone": "...",
  "urgency": "...",
  "suggested_reply": "...",
  "summary": "..."
}}

Email:
\"\"\"{email_text}\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an email sentiment analysis tool.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=500,
        )

        content = response.choices[0].message.content.strip()
        return (
            eval(content)
            if content.startswith("{")
            else {"error": "Unexpected response"}
        )

    except Exception as e:
        return {"error": str(e)}
