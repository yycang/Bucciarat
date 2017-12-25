#########
# 选择排序
#########

"""

算法原理:
比较简单直观, 就是在未排序序列寻找最小(或者最大值), 放在起始(或者末尾位置)作为已排序序列
持续上述步骤, 直到所有已排序

"""


def selection_sort(li):
    n = len(li)
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1的到末尾选出最小数
        for j in range(i+1, n):
            if li[j] < li[min_index]:
                min_index = j

        # 如果选出的不在正确的位置上
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]

li = [4, 5, 7, 1, 12, 323, 55, 32]
selection_sort(li)
print(li)

"""

时间复杂度:
        最优时间复杂度: O(n^2)
        最坏时间复杂度: O(n^2)
        稳定性:    不稳定

"""

