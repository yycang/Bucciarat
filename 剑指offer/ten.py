# 斐波那契数列


def fibonacci(n):
    one = 1
    two = 0

    if n == 0:
        return two
    if n == 1:
        return one

    x = 2
    while x <= n:
        fib = one + two
        two, one = one, fib
        x += 1
        print(fib)
    return fib


if __name__ == '__main__':
    print(fibonacci(5))
