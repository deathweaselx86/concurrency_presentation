import argparse
from threading import Thread

def trial_division(n):
    divisors = []
    current_factor = 2
    while n > 1:
        if (n % current_factor == 0):
            divisors.append(current_factor)
            n /= current_factor
        else:
            current_factor += 1
    print(divisors)

def get_divisors(numbers):
    threads = []
    for n in numbers:
        t = Thread(target=trial_division, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    get_divisors([907141, 907142, 907143, 907144, 907145])
