import argparse
import asyncio

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

async def get_divisor(n):
    print(n,': ',trial_division(n))

def get_divisors(numbers):
    loop = asyncio.get_event_loop()
    tasks = []
    for n in numbers:
        tasks.append(asyncio.ensure_future(get_divisor(n)))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='factoring')
    parser.add_argument('numbers', metavar='N', type=int, nargs=5)
    args = parser.parse_args()

    get_divisors(args.numbers)
