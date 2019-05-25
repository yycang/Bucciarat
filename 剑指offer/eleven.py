# 旋转数组中的最小数字


def find_min_in_arr(num):
    p1 = 0
    p2 = len(num) - 1
    min_val = num[0]

    while num[p1] >= num[p2]:
        if p2 - p1 == 1:
            return num[p2]

        mid = (p1 + p2) // 2
        if num[mid] == num[p1] == num[p2]:
            for i in range(len(num)):
                if num[i] < min_val:
                    min_val = num[i]
            return min_val

        if num[mid] >= num[p1]:
            p1 = mid
        else:
            p2 = mid
    return num[p2]


if __name__ == '__main__':
    print(find_min_in_arr([3, 4, 5, 1, 2]))
    print(find_min_in_arr([1, 1, 1, 0, 1]))
