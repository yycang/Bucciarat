# 机器人移动，地上有m行和n列的方格，机器人从0，0开始移动，每次只能移动上下左右一格
# 不能进入行左标+列左标大于k的格子，例如k=18，不能进入方格（35，38），因为3+5+3+8=19
# 机器人能够到达多少个格子


def moving_count(k, rows, cols):
    if k < 0 or rows < 0 or cols < 0:
        return False

    visited = [0] * (rows * cols)
    count = moving_count_core(k, rows, cols, 0, 0, visited)
    return count


def moving_count_core(k, rows, cols, row, col, visited):
    count = 0
    if check(k, rows, cols, row, col, visited):
        visited[row * cols + col] = 1
        count = 1 + moving_count_core(k, rows, cols, row, col - 1, visited) + \
            moving_count_core(k, rows, cols, row, col + 1, visited) + \
            moving_count_core(k, rows, cols, row - 1, col, visited) + \
            moving_count_core(k, rows, cols, row + 1, col, visited)
    return count


def check(k, rows, cols, row, col, visited):
    if rows > row >= 0 and cols > col >= 0 and get_digit_sum(row) + get_digit_sum(col) <= k and \
            visited[row * cols + col] == 0:
        return True
    return False


def get_digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


if __name__ == '__main__':
    print(moving_count(5, 5, 5))

