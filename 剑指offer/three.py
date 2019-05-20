# 找出数组中重复的数字


def duplicate(arr):
    if not arr or len(arr) == 0:
        return False

    for i in range(len(arr)):
        while arr[i] != i:
            if arr[i] == arr[arr[i]]:
                return True
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
    return False


# 长度为n+1的数组中所有数字在1～n范围内，必定有重复数字，找出数组中任意的重复数字
def duplicate2(arr):
    arr2 = [None] * len(arr)
    for i in range(len(arr)):
        if arr2[arr[i]] is None:
            arr2[arr[i]] = arr[i]
        else:
            return arr[i]


if __name__ == '__main__':
    lst = [1, 2, 4, 2, 5, 1, 2, 3]
    print(duplicate(lst))

    lst2 = [2, 1, 3, 6, 5, 6, 4]

    print(duplicate2(lst2))
