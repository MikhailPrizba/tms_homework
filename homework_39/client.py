import asyncio

import aiohttp


async def main():
    async with aiohttp.ClientSession('http://localhost:9999') as session:

            text = input('Enter question: ')
            headers = {'Content-Type': 'application/json'}
            async with session.post('/v1',json= {'text': text}, headers=headers) as resp:
                print(await resp.text())

asyncio.run(main())