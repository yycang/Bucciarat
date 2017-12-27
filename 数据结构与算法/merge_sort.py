#########
# 归并排序
#########

"""

算法原理:
1.归并排序是分治法的一个典型思想, 即先递归的分解数组, 然后再重组数组
2.将数组分解为最小后, 然后合并两个有序数组, 比较两个数组前面的数, 谁小取谁

"""


def merge_sort(li):
    if len(li) <= 1:
        return li

    # 分解
    num = len(li) // 2
    left = merge_sort(li[:num])
    right = merge_sort(li[num:])

    # 合并
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result


li = [4, 5, 1, 11, 9, 12, 44, 19]
li2 = merge_sort(li)
print(li2)


"""

时间复杂度:
        最优时间复杂度: O(nlogn)
        最坏时间复杂度: O(nlogn)
        稳定性:    稳定

"""