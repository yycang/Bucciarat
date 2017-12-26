#########
# 快速排序
#########

"""

算法原理:
1.从数组中挑选一个数为基准, 排序数组, 比基准小的放在数组左边, 比基准大的放在数组右边
2.递归的把基准左边的数组和基准右边的数组进行排序

"""


def quick_sort(li, s, e):
    # 退出递归
    if s >= e:
        return
    m = li[s]
    low = s     # 从左到右移动的游标
    high = e    # 从右往左移动的游标

    while low < high:
        # 如果右边的游标和基准比较, 比他大的话就减一(向左移动)
        while low < high and li[high] >= m:
            high -= 1
        li[low] = li[high]

        # 左边的游标和基准比较, 如果比他小的话就加一(向右移动)
        while low < high and li[low] < m:
            low += 1
        li[high] = li[low]

    # 退出循环后, 游标重合, 放到正确的基准位置
    li[low] = m

    quick_sort(li, s, low-1)
    quick_sort(li, low+1, e)

li = [9, 5, 1, 12, 44, 2, 52, 123]
quick_sort(li, 0, len(li)-1)
print(li)


"""

时间复杂度:
        最优时间复杂度: O(nlogn)
        最坏时间复杂度: O(n^2)
        稳定性: 不稳定

"""