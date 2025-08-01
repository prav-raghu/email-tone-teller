from fastapi import APIRouter
from app.dtos.analyze_dto import EmailRequest
from app.services.sentiment import analyze_email
from app.utilities.logger import logger

router = APIRouter(prefix="/analyze", tags=["Analysis"])


@router.post("/")
async def analyze(request: EmailRequest):
    result = analyze_email(request.text)

    if "error" in result:
        logger.error(f"Failed to analyze email: {result['error']}")
        return {"status": "error", "message": "internal server error"}

    logger.info(f"Email Analyzed: {result}")
    return {result}
