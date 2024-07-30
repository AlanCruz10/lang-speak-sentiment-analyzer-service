from fastapi import APIRouter, status

from src.application.dtos.requests.analyze_message_request import AnalyzeMessageRequest
from src.application.services.analyzer_service import AnalyzerService
from src.application.services.use_cases.analyze_message_use_case import AnalyzeMessageUseCase
from src.application.utilities.sentiment_analyze_models import analytic_sentiments_multilingual

message_use_case = AnalyzeMessageUseCase(analytic_sentiments_multilingual)
service = AnalyzerService(message_use_case)

router = APIRouter()


@router.post("/v1/analyzer", status_code=status.HTTP_200_OK)
async def create_chat(request: AnalyzeMessageRequest):
    return service.analyze(request)
