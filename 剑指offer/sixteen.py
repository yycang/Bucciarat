# 实现函数求base的exponent次方，不得使用库函数


def calc(base, exponent):
    if base == 0 and exponent < 0:
        return 0
    if exponent >= 0:
        return power(base, exponent)
    else:
        return 1 / power(base, -exponent)


def power(base, exponent):

    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = power(base, exponent >> 1)
    result *= result
    if exponent & 0x1 == 1:
        result *= base

    return result


if __name__ == '__main__':
    print(calc(2, -3))
    print(calc(2, 0))
    print(calc(-2, 3))
    print(calc(-2, -3))
