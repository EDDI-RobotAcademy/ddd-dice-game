from dice.application.dice_service_impl import DiceServiceImpl
from fastapi import APIRouter

dice_router = APIRouter()
dice_service: DiceServiceImpl = DiceServiceImpl()  # 인터페이스 기반으로 타입 지정 가능

@dice_router.get("/roll")
def roll_dice():
    result = dice_service.roll_dice()
    return {"result": result}
