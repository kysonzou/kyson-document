---
category:
- Tech
tags:
- Algorithms
status: Done
---



• **定义**：冒泡排序是一种简单的交换排序算法。它通过重复比较相邻的两个元素，并根据需要交换它们的位置，将最大的元素“冒泡”到数组末尾。每次迭代完成后，未排序的部分长度减一。

• **时间复杂度**：O(n²)，其中 n 是数组的长度。

• **优点**：实现简单，适合初学者理解。

• **缺点**：效率低，尤其在数据规模较大时表现极差。

```python
def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制总共要进行几轮排序
    for i in range(n):
        swapped = False  # 标记当前是否发生了交换
        # 内层循环用于进行一轮“冒泡”
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 如果前面的元素大于后面的元素，就交换它们
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # 标记发生了交换
        # 如果某一轮遍历中没有发生任何交换，说明数组已经有序，直接结束
        if not swapped:
            break

# 测试用例
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
```