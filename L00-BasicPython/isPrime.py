import math


# ~ Big O(n)
def is_prime(num: int) -> bool:
    if not isinstance(num, int):
        return False

    if num < 2:
        return False

    end = num

    for i in range(2, end, 1):
        if num % i == 0:
            return False

    return True


# ~ Big O(n/2)
def is_prime2(num: int) -> bool:
    if not isinstance(num, int):
        return False

    if num < 2:
        return False

    end = int(num / 2)

    for i in range(2, end + 1, 1):
        if num % i == 0:
            return False

    return True


# ~ Big O(n/4)
def is_prime3(num: int) -> bool:
    if not isinstance(num, int):
        return False

    if num < 2:
        return False

    if num == 2 or num == 3:
        return True

    end = num // 2

    if num % 2 == 0:
        return False

    for x in range(3, end, 2):
        if num % x == 0:
            return False

    return True


# ~Big O(sqrt(n)/2)
def is_prime4(num: int) -> bool:
    if not isinstance(num, int):
        return False

    if num < 2:
        return False

    if num == 2 or num == 3:
        return True

    end = int(math.sqrt(num))

    if num % 2 == 0:
        return False

    for x in range(3, end, 2):
        if num % x == 0:
            return False

    return True


for i in range(0, 1001, 1):
    if is_prime(i) != is_prime2(i) != is_prime3(i) != is_prime4(i):
        print(i, is_prime(i), is_prime2(i), is_prime3(i), is_prime4(i))

print('End Ja')
