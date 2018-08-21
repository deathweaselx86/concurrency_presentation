#!/usr/local/bin/python3 
import requests

def search(query):
    print('Searching for %s' % query)
    req = requests.get('http://google.com/search', params={ 'q': query  })

def get_searches(searches):
    for query in searches:
        search(query.strip())

if __name__ == '__main__':
    get_searches(['dog','cat','ferret', 'betta', 'rabbit'])
