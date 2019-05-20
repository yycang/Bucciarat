# 二维数组，每行都是从左到右递增，每列都是从上到下递增，判断该数组是否有某个整数


def find_num(arr, num):
    cur_col = 0
    row = len(arr) - 1
    col = len(arr[0]) - 1

    while cur_col <= col and row >= 0:
        if arr[row][cur_col] == num:
            return True
        if arr[row][cur_col] > num:
            row -= 1
        if arr[row][cur_col] < num:
            cur_col += 1
    return False


if __name__ == '__main__':
    arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(find_num(arr, 7))
    print(find_num(arr, 5))

