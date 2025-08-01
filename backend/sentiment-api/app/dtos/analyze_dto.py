from pydantic import BaseModel


class EmailRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    tone: str
    urgency: str
    summary: str
    suggested_reply: str
