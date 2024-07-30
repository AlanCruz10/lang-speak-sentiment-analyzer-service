from abc import ABC

from src.application.dtos.requests.analyze_message_request import AnalyzeMessageRequest
from src.application.dtos.responses.base_response import BaseResponse
from src.application.ports.inputs.analyzer_service_port_input import AnalyzerServicePortInput


class AnalyzerService(AnalyzerServicePortInput):

    def __init__(self, analyzer_message_use_case):
        self.analyzer_message_use_case = analyzer_message_use_case

    def analyze(self, request: AnalyzeMessageRequest):

        execute = self.analyzer_message_use_case.execute(request)

        response = BaseResponse(data=execute, message="Message analyzed successfully.", success=execute.muted, status_code=200,
                                http_status="OK")
        return response
