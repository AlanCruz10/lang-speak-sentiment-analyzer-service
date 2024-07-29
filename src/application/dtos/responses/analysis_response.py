import json
from dataclasses import dataclass


@dataclass
class AnalysisResponse:
    uuid: str
    content: str
    sentiment: str
    score: float
    type: str
    user_id: str
    muted: bool

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'content': self.content,
            'sentiment': self.sentiment,
            'score': self.score,
            'type': self.type,
            'user_id': self.user_id,
            'muted': self.muted
        }

    def to_json(self):
        return json.dumps(self.to_dict())
