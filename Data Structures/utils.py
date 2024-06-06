def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def previous_prime(number):
    if number < 2:
        raise ValueError("invalid number")
    while number >= 2:
        number -= 1
        if is_prime(number):
            return number
    raise ValueError("invalid number")


def next_prime(number):
    if number <= 1:
        return 2
    next_number = number + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1


def hash1(key, length):
    if isinstance(key, int):
        return key % length
    raise ValueError("key cannot be hashed")


def hash2(key, length):
    if isinstance(key, int):
        prime = previous_prime(length)
        return prime - (key % prime)
    raise ValueError("key cannot be hashed")


def indexify(length, index):
    if index > length:
        index = length
    elif index < 0:
        index = length - abs(index)
        if index < 0:
            index = 0
    return index
