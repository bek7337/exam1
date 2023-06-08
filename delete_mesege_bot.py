from aiogram import types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State,StatesGroup
class State1(StatesGroup):
    state1=State()
def unli_tek(a):
    s=0
    unlilar="euioaAEUIO"
    for i in a:
        if i in unlilar:
            s+=1
    if s>=5:
        return True
    else:return False
BOT_TOKEN = '5917312329:AAFfeJ_5r2WN8CxpYDLWk_q2QVLcS-IcbDs'
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot,storage=MemoryStorage())
@dp.message_handler(commands='start')
async def start(msg:types.Message):
    s = f"Assalom alekom <b>{msg.from_user.first_name}</b> So`zni kiriting"
    await msg.answer(text=s,parse_mode='html')
    await bot.set_my_commands([BotCommand('start',"Ishga Tushirish")])
    await State1.state1.set()
@dp.message_handler(state=State1.state1)
async def message_och(msg:types.Message):
    s=unli_tek(msg.text)
    if s==True:
        s=f"Hurmatli mijoz kiritlgan ma`lumotda unli harf 5 tadan ko`p"
        await msg.answer(text=s,parse_mode='html')
        await msg.delete()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # docker - compose
    # up
    # 612
    # sudo
    # apt
    # install
    # docker - compose