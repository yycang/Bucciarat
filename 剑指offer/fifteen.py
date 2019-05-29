# 输出该数二进制中1的个数，比如9的二进制是1001


def num_count(n):
    count = 0
    while n:
        count += 1
        print(n)
        n = n & (n - 1)
        print(n, '*')
    return count


if __name__ == '__main__':
    print(num_count(9))

