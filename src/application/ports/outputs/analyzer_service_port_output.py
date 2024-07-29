from abc import ABC, abstractmethod
from src.domain.entities.message import Message
from src.domain.repositories.message_repository import MessageRepository


class AnalyzerServicePortOutput(MessageRepository, ABC):

    @abstractmethod
    def analyze_message(self, message: str) -> tuple:
        pass
