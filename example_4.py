import trio
import time


def slow_add(x, y):
    time.sleep(2)
    print(f'{x}+{y}={x+y}')
    return x + y


async def async_slow_add(x, y):
    return await trio.to_thread.run_sync(slow_add, x, y)


async def slow_hello():
    await trio.sleep(1)
    print('hi')


async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(async_slow_add, 1, 2)
        nursery.start_soon(slow_hello)
    return 'done'

r = trio.run(main)
