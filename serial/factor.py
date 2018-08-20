import argparse

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

def get_divisors(numbers):
    for n in numbers:
        print(n,': ',trial_division(n))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='factoring')
    parser.add_argument('numbers', metavar='N', type=int, nargs=5)
    args = parser.parse_args()
    get_divisors(args.numbers)
