# app/routes/analyze.py
from fastapi import APIRouter, HTTPException
from app.dtos.analyze_dto import EmailRequest
from app.services.sentiment import analyze_email
from app.utilities.logger import logger

router = APIRouter(prefix="/analyze", tags=["Analysis"])


@router.post("/")
async def analyze(request: EmailRequest):
    try:
        result = await analyze_email(request.subject, request.body)

        if "error" in result:
            logger.error(f"Failed to analyze email: {result['error']}")
            raise HTTPException(status_code=500, detail="internal server error")

        logger.info(f"Email Analyzed: {result}")
        return {"data": result}
    except Exception as e:
        logger.exception("Analyze endpoint crashed", e)
        raise HTTPException(status_code=500, detail="internal server error")
