# session을 만들지 않고 HTTP Request를 전송할 수도 있음.
import aiohttp
import asyncio


async def main():
    async with aiohttp.request('GET', "http://python.org/") as rsp:
        print(rsp.status)
        print(rsp.headers)
        print(await rsp.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())