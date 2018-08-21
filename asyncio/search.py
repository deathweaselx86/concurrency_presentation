#!/usr/local/bin/python3 
import argparse
import requests
import asyncio

async def search(query):
    print('Searching for %s' % query)
    req = requests.get('http://google.com/search', params={ 'q': query  })

def get_searches(searches):
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(search(query)) for query in searches]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    get_searches(['dog','cat','ferret', 'betta', 'rabbit'])
