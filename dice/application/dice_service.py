from abc import ABC, abstractmethod

class DiceService(ABC):
    """애플리케이션 서비스 인터페이스"""

    @abstractmethod
    def roll_dice(self) -> int:
        pass
