import trio


async def main():
    print("Hello, World!")
    await trio.sleep(1)
    print("Goodbye, World!")

trio.run(main)
