import asyncio
import aiohttp

async def search(session, query):
    print('Searching for %s' % query)
    response = await session.get('http://google.com/search', params={ 'q': query })
    return await response.release()

async def get_searches(loop, searches):
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [search(session, query) for query in searches]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_searches(loop, ['dog','cat','ferret', 'betta', 'rabbit']))
