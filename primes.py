"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = [2]
    num = 3
    if number_of_primes < 1:
        raise ValueError
    else:
        while len(list) < number_of_primes:
            if num % 2 != 0:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
            num += 1

    return list
