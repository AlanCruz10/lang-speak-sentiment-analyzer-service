from abc import ABC, abstractmethod
from src.domain.entities.message import Message


class MessageRepository(ABC):

    @abstractmethod
    def analyze_message(self, message: Message) -> tuple:
        pass
