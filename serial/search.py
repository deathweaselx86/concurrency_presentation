#!/usr/local/bin/python3 
import argparse
import requests
import timeit

def search(query):
    print('Searching for %s' % query)
    req = requests.get('http://google.com/search', params={ 'q': query  })
    print('Saving %s query to file %s.txt' %  (query, query))
    searchFile = '%s.txt' % query
    with open(searchFile, 'w') as searchOutput:
        searchOutput.write(req.text)

def get_searches(filename):
    with open(filename, 'r') as searches:
        for query in searches:
            query = query.strip()
            search(query)

def fake_print(string):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='searching')
    parser.add_argument('filename', metavar='f', type=str, help='a file to read')
    args = parser.parse_args()
    get_searches(args.filename)