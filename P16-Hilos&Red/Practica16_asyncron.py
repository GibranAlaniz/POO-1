import asyncio

async def tarea(nombre):
    print(f"{nombre} inicia ")
    await asyncio.sleep(2)
    print(f"{nombre} termina")

async def main():
    await asyncio.gather(
        tarea("tareal"),
        tarea("tareal2")
    )
asyncio.run(main())