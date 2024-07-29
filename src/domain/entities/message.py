from dataclasses import dataclass


@dataclass
class Message:
    uuid: str
    type: str
    content: str | None
    user_id: str
