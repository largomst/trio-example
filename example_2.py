import trio
import time


async def child1():
    print("Child 1: started!")
    await trio.sleep(1)
    print("Child 1: exiting!")


async def child2():
    print("Child 2: started!")
    await trio.sleep(1)
    print("Child 2: exiting!")


async def parent():
    print("Parent: started!")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child1)
        nursery.start_soon(child2)
    print("Parent: exiting!")


start = time.perf_counter()
trio.run(parent)
cost = time.perf_counter() - start
print(cost)
