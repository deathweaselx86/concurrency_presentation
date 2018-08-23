import requests
from threading import Thread

def search(query):
    print('Searching for %s' % query)
    req = requests.get('http://google.com/search', params={ 'q': query  })

def get_searches(searches):
    threads = []
    for query in searches:
        t = Thread(target=search, args=(query,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == '__main__':
    get_searches(['dog','cat','ferret', 'betta', 'rabbit'])
