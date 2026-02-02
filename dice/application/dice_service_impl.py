from dice.application.dice_service import DiceService
from dice.domain.dice import Dice


class DiceServiceImpl(DiceService):
    """DiceService 구현체"""

    def __init__(self):
        self.dice = Dice()

    def roll_dice(self) -> int:
        return self.dice.roll()
