from pydantic import BaseModel


class EmailRequest(BaseModel):
    subject: str
    body: str


class SentimentResponse(BaseModel):
    tone: str
    urgency: str
    summary: str
    suggested_reply: str
