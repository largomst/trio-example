import trio
import queue


async def child1(q):
    await trio.sleep(1)
    q.put(1)


async def child2(q):
    await trio.sleep(1)
    q.put(2)


async def parent():
    q = queue.Queue()

    async with trio.open_nursery() as nursery:
        nursery.start_soon(child1, q)
        nursery.start_soon(child2, q)
    while not q.empty():
        print(q.get())


trio.run(parent)
