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


if __name__ == '__main__':
    lst = [1, 2, 4, 2, 5, 1, 2, 3]
    print(duplicate(lst))
