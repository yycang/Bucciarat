# 输入数字n，按顺序打印从1到最大n位的十进制数字


def result(n):
    if n <= 0:
        return
    number = [0] * n
    for i in range(10):
        number[0] = str(i)

        print_max_num(number, n, 0)


def print_num(number):
    is_begin_zero = True
    for i in range(len(number)):
        if is_begin_zero and number[i] != '0':
            is_begin_zero = False
        if not is_begin_zero:
            print(number[i])
    print('\t')


def print_max_num(number, length, index):
    print(number)
    if index == length - 1:
        print_num(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        print_max_num(number, length, index + 1)


if __name__ == '__main__':
    result(2)
