# 将一段字符串中每个空格替换成"%20"


def replace_string(s):
    new_string = ''
    for i in s:
        if i == ' ':
            new_string += "%20"
        else:
            new_string += i

    return new_string


if __name__ == '__main__':
    s = "we are happy"
    print(replace_string(s))
