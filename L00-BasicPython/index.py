true = True
false = False


def factorial(num: int)-> int:
    if num == 2:
        return num

    return factorial(num - 1) * num


def is_int(num_str: str) -> bool:
    try:
        int(num_str)
        return true
    except ValueError:
        return false


def input_int_from_cli(label) -> int:
    _x = input(label)

    while not is_int(_x):
        print('Invalid Input Number')
        _x = input(label)

    return int(_x)


print('Enter your INTEGER value of X and press Enter')
x = input_int_from_cli('X: ')
print('Enter your INTEGER value of Y and press Enter')
y = input_int_from_cli('Y: ')

print('X + Y = ', x + y)
print('X - Y = ', x - y)
print('X * Y = ', x * y)
print('X ^ Y = ', x ^ y)
print('X! = ', factorial(x))
print('Y! = ', factorial(y))
if y != 0:
    print('X / Y = ', x / y)
    # Floor Division -
    # The division of operands where the result is the quotient in which the digits after the decimal point are removed.
    # But if one of the operands is negative, the result is floored,
    # i.e., rounded away from zero (towards negative infinity):
    print('X // Y = ', x // y)
    print('X % Y = ', x % y)
