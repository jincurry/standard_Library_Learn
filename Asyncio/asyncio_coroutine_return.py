import asyncio


async def coroutine():
    print('in coroutine')
    return 'result'


event_loop = asyncio.get_event_loop()
try:
    print('Starting')
    return_value = event_loop.run_until_complete(
        coroutine()
    )
    print('return from coroutine')
    print('it returned: {!r}'.format(return_value))
finally:
    event_loop.close()
