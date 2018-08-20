import argparse
from multiprocessing import Process

def trial_division(n):
    divisors = []
    current_factor = 2
    while n > 1:
        if (n % current_factor == 0):
            divisors.append(current_factor)
            n /= current_factor
        else:
            current_factor += 1
    if divisors:
        return divisors
    else:
        return 'prime'

def get_divisor(n):
    print(n,': ',trial_division(n))

def get_divisors(numbers):
    processes = []
    for n in numbers:
        p = Process(target=get_divisor, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='factoring')
    parser.add_argument('numbers', metavar='N', type=int, nargs=5)
    args = parser.parse_args()
    get_divisors(args.numbers)
