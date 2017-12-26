##########
# 二分查找
##########


"""

算法原理:
1.需在一个有序的数组中, 按照中间的数和要查找的数做比较, 如果两者相等则查找成功
2.否则利用中间位置将数组分为两个部分, 如果中间的数比要查找的数大, 则往前一个部分数组中进一步查找, 否则往后一部分数组中进行查找
3.重复以上过程, 如果查找到数组不存在, 则查找失败

"""


# 非递归实现
def binary_search(li, num):
    first = 0
    last = len(li)-1
    while first <= last:
        # 判定中位数
        m = (first + last) // 2
        if li[m] == num:
            return True
        elif num < li[m]:
            last = m - 1
        else:
            first = m + 1
        # 很简单的逻辑, 如果查找的数比中位数要小, 那么数组在左边, 则把范围划分到左边, 反之则划分到右边
    return False


# 递归实现
def binary_search2(li, num):
    if len(li) == 0:
        return False
    else:
        m = len(li) // 2
        if li[m] == num:
            return True
        else:
            # 递归实现套路一样, 只不过要记得切片是左闭右开, 递归右边的时候要从中位数+1开始
            if num < li[m]:
                return binary_search2(li[:m], num)
            else:
                return binary_search2(li[m+1:], num)


li = [1, 3, 5, 9, 12, 15, 111, 154, 189, 201, 222, 1211]
print(binary_search(li, 2))
print(binary_search2(li, 201))
