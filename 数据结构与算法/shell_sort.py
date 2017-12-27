#########
# 希尔排序
#########

"""

算法原理:
1.核心思想以步长为间隔进行比较, 比如第一次设置步长为5, 第一个元素和第六个元素进行比较
2.然后步长减少, 以步长为2进行排序, 即第一个元素和第三个元素进行比较
3.最后步长为1进行比较, 此时就是简单的插入排序了

"""


def shell_sort(li):
    n = len(li)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and li[j-gap] > li[j]:
                li[j-gap], li[j] = li[j], li[j-gap]
                j -= gap
        gap //= 2

li = [5, 10, 12, 1, 4, 123]
shell_sort(li)
print(li)

"""

时间复杂度:
        最优时间复杂度: 根据步长来决定
        最坏时间复杂度: O(n^2)
        稳定性:    不稳定

"""