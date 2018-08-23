import requests
from multiprocessing import Process

def search(query):
    print('Searching for %s' % query)
    req = requests.get('http://google.com/search', params={ 'q': query  })

def get_searches(searches):
    processes = []
    for query in searches:
        p = Process(target=search, args=(query.strip(),))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

if __name__ == '__main__':
    get_searches(['dog','cat','ferret', 'betta', 'rabbit'])
