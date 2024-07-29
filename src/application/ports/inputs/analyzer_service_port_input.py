from abc import abstractmethod, ABC

from src.application.dtos.requests.analyze_message_request import AnalyzeMessageRequest
from src.application.dtos.responses.base_response import BaseResponse


class AnalyzerServicePortInput(ABC):

    @abstractmethod
    def analyze(self, request: AnalyzeMessageRequest) -> str:
        pass
