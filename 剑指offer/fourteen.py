# 剪绳子问题，给长度为n的绳子，要求剪m段，每段都为整数，如何剪出每段绳子的最大乘积


def max_count(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    # 创建长度为length的数组存储子问题的最优解
    f = [None for _ in range(length + 1)]
    f[0], f[1], f[2], f[3] = 0, 1, 2, 3
    res = 0
    for i in range(4, length+1):
        for j in range(1, (i // 2) + 1):
            temp = f[j] * f[i - j]
            if temp > res:
                res = temp

        f[i] = res
    return res


def max_count_2(length):
    # 贪婪解法
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    # 尽可能去剪长度为3的绳子段，当剩下长度为4时不能继续剪，因为3*1<2*2
    count = length // 3
    if (length - count * 3) == 1:
        count -= 1
    count2 = (length - count * 3) // 2
    return (3 ** count) * (2 ** count2)


if __name__ == '__main__':
    print(max_count(8))
    print(max_count_2(4))
