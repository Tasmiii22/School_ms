import asyncio

async def make_coffee():
    print("Brewing Coffee")
    await asyncio.sleep(2)
    print("Coffee Ready")

async def make_toast():
    print("Toasting bread")
    await asyncio.sleep(2)
    print("Toast Ready")

async def breakfast():
    await asyncio.gather(make_coffee(), make_toast())

asyncio.run(breakfast())
