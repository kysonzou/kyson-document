---
category:
- Tech
tags:
- Algorithms
status: Done
---



- **定义**：归并排序是一种基于分治思想的递归排序算法。它将待排序数组分成两半，分别进行排序，然后通过合并操作将两部分组合成一个有序数组。

- **时间复杂度**：O(n log n)。

- **优点**：稳定排序算法，不受最坏情况的影响（即无论输入数据如何，它都能保持 O(n log n) 的复杂度）。

- **缺点**：需要额外的 O(n) 空间来存储中间结果。

**代码示例：**

```python
# 递归排序
def merge_sort(arr):
    # 基本条件：数组长度小于等于 1 时，返回该数组
    if len(arr) <= 1:
        return arr

    # 分割数组为两部分
    mid = len(arr) // 2  # 找到数组的中间位置
    left_half = merge_sort(arr[:mid])  # 对左半部分递归排序
    right_half = merge_sort(arr[mid:])  # 对右半部分递归排序

    # 合并两个有序的子数组
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []  # 存储合并后的有序数组
    i = j = 0

    # 比较 left 和 right 两个数组的元素，依次放入 sorted_array 中
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # 如果有剩余元素，直接加到结果数组中
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# 测试用例
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
```