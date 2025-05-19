---
category:
- Tech
tags:
- Algorithms
status: Done
---




 **快速排序（QuickSort）** 是一种非常高效的基于分治策略的排序算法。它通过选择一个“**基准（pivot）**”元素，将数组划分为两部分：小于基准的元素放在左边，大于基准的元素放在右边。然后分别递归地对左右子数组进行排序。

 **快速排序的步骤：**

   1. **选择基准（pivot）**：从数组中选一个元素作为基准，可以是第一个、最后一个、中间的元素或随机选取。
   
   2. **划分数组**：将数组中小于基准的元素放在基准的左边，大于基准的元素放在基准的右边。
   
   3. **递归排序**：对基准左边和右边的两个子数组分别应用快速排序，直到子数组的长度为 1 或 0，表示它们已经有序。
   
   4. **合并**：由于排序是在原地进行，不需要像归并排序那样合并，数组在每次递归后自然变得有序。

**python代码：**

```python
def quick_sort(arr):
    # 递归基准：如果数组长度小于等于 1，直接返回
    if len(arr) <= 1:
        return arr
    else:
        # 选择基准（这里选择数组的最后一个元素作为基准）
        pivot = arr[-1]
        
        # 小于基准的元素放在左边，大于基准的元素放在右边
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
        # 递归对左右两部分排序，并将它们与基准合并
        return quick_sort(left) + [pivot] + quick_sort(right)

# 测试用例
arr = [10, 80, 30, 90, 40, 50, 70]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
```
  
```python
# 原地快速排序的实现,不占用额外的内存空间
def quick_sort_in_place(arr, low, high):
    if low < high:
        # 找到分区点
        pivot_index = partition(arr, low, high)
        # 对左右两部分递归排序
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # i 表示小于 pivot 的区域的最后一个元素
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素，保证小于 pivot 的在左边
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 把 pivot 放到正确位置
    return i + 1

# 测试用例
arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort_in_place(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
```

**快速排序的特点：**

- **时间复杂度**：

   - 平均情况下，快速排序的时间复杂度为 O(n log n)，这也是其在大多数情况下表现优秀的原因。

   - 最坏情况下（即每次划分都导致最不平衡的划分，如数组已经有序或逆序的情况），时间复杂度会退化为 O(n²)。不过，通常通过优化基准的选择，可以避免最坏情况的发生。

• **空间复杂度**：O(log n)（递归调用栈的深度）。

• **不稳定排序**：在快速排序中，元素的相对位置可能会改变，因此它是一个不稳定的排序算法。

总的来说，**快速排序** 是一种非常高效的排序算法，尤其适用于大数据集。