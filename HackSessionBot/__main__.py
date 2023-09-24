import asyncio
import importlib

from pyrogram import idle
from HackSessionBot import LOG
from HackSessionBot.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("HackSessionBot.modules." + all_module)
    LOG.print("[bold yellow]✨ شتغل")
    await idle() 
    LOG.print("[bold red]القناة تم مثل ما طلبت.")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
