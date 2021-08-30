import trio


async def aenumerate(aiterable, start=0):
    async for i in aiterable:
        yield start, i
        start += 1


async def send_messages(sc):
    for i in range(10):
        print(f"sending {i}")
        await sc.send(b"hello")


async def recv_messages(rc):
    async for i, msg in aenumerate(rc):
        print(f"received {i}:")


async def main():
    sc, rc = trio.open_memory_channel(0)
    async with trio.open_nursery() as nursery:
        nursery.start_soon(send_messages, sc)
        nursery.start_soon(recv_messages, rc)

trio.run(main)
