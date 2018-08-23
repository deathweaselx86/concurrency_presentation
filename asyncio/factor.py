import asyncio

async def trial_division(n):
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
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(trial_division(n)) for n in numbers]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    get_divisors([907141, 907142, 907143, 907144, 907145])
