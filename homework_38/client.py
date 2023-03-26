import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession('http://0.0.0.0:8080') as session:
        
            question = input('Enter question: ')
            headers = {'Content-Type': 'application/json'}
            async with session.post('/',json= {'question': question}, headers=headers) as resp:
                print(await resp.text())
            
asyncio.run(main())