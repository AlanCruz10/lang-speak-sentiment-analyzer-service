from dataclasses import dataclass


@dataclass
class AnalyzeMessageRequest:
    uuid: str
    content: str
    type: str
    user_id: str
