#!/usr/local/bin/python3 
import argparse
import requests
from threading import Thread

def search(query):
    print('Searching for %s' % query)
    req = requests.get('http://google.com/search', params={ 'q': query  })
    print('Saving %s query to file %s.txt' %  (query, query))
    searchFile = '%s.txt' % query
    with open(searchFile, 'w') as searchOutput:
        searchOutput.write(req.text)

def get_searches(filename):
    threads = []
    with open(filename, 'r') as searches:
        count = 0
        for query in searches:
            query = query.strip()
            t = Thread(target=search, name=count, args=(query,))
            count = count+1
            t.start()
            threads.append(t)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Counting in ranges of 5')
    parser.add_argument('filename', metavar='f', type=str, help='a file to read')
    
    args = parser.parse_args()
    get_searches(args.filename)
