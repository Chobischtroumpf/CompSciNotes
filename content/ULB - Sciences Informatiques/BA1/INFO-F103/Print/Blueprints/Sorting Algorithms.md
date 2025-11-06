---
title: Sorting Algorithms
authors: Alessandro Dorigo
tags:
  -
---

# Bubble Sort
```python
def bubble_sort(array):
    for end_idx in range(len(array) - 1, 0, -1):
        for curr in range(end_idx):
            if array[curr] > array[curr + 1]:
                array[curr], array[curr + 1] = array[curr + 1], array[curr]


def optimized_bubble_sort(array):
    swapped = True
    last_unsorted_idx = len(array) - 1

    while last_unsorted_idx > 0 and swapped:
        swapped = False

        for curr in range(last_unsorted_idx):
            if array[curr] > array[curr + 1]:
                swapped = True
                array[curr], array[curr + 1] = array[curr + 1], array[curr]

        last_unsorted_idx -= 1
```
# Insertion Sort
```python
def insertion_sort(array):
    for i in range(1, len(array)):
        curr_val = array[i]
        curr_pos = i - 1

        while curr_pos >= 0 and array[curr_pos] > curr_val:
            array[curr_pos + 1] = array[curr_pos]
            curr_pos -= 1

        array[curr_pos + 1] = curr_val
```
# Merge Sort
```python
def merge_sort(array):
    print("Splitting", array)

    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_idx = 0
        right_idx = 0
        merged_idx = 0

        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                array[merged_idx] = left_half[left_idx]
                left_idx += 1
            else:
                array[merged_idx] = right_half[right_idx]
                right_idx += 1
            merged_idx += 1

        while left_idx < len(left_half):
            array[merged_idx] = left_half[left_idx]
            left_idx += 1
            merged_idx += 1

        while right_idx < len(right_half):
            array[merged_idx] = right_half[right_idx]
            right_idx += 1
            merged_idx += 1

    print("Merging", array)
```
# Quick Sort
```python
from Blueprints.Sorts.Insertion_Sort import insertion_sort

# Simple Quick Sort
class SimpleQuickSort:
    def __init__(self, array, type=1):
        self.array = array
        self.type = type
        self.quick_sort(0, len(self.array) - 1)
        print(self.array)

    def partition(self, type, l, r, array):
        if type == 1:
            return self.partition_left(l, r, array)
        else:
            return self.partition_right(l, r, array)

    def quick_sort(self, l, r):
        if l < r:
            pivot = self.partition(self.type, l, r, self.array)
            self.quick_sort(l, pivot - 1)
            self.quick_sort(pivot + 1, r)

    def partition_right(self, l, r, array):
        pivot = array[r]  # Choose the last element as the pivot
        i = l - 1

        for j in range(l, r):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

    def partition_left(self, l, r, array):
        pivot = array[l]  # Choose the first element as the pivot
        i = l + 1
        j = r

        while True:
            while i <= j and array[i] <= pivot:
                i += 1
            while j >= i and array[j] >= pivot:
                j -= 1

            if i >= j:
                break
		    array[i], array[j] = array[j], array[i]

        array[l], array[j] = array[j], array[l]
        return j

# Quick Sort with Insertion Sort + Pivot Optimization
class QuickSort:
    def __init__(self, array):
        self.array = array
        self.threshold = 16
        self.quick_sort(0, len(self.array) - 1)
        self.insertion_sort = insertion_sort(self.array)
        print(self.array)

    def partition(self, start, end):
        pivot = self.array[end]
        i = start - 1

        for j in range(start, end):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[end] = self.array[end], self.array[i + 1]
        return i + 1

    # Optimized pivot, based on median of three:
    # 1. Choose the first, middle and last elements from array
    # 2. Sort them and choose the middle element as the pivot
    def optimize_pivot(self, start, end):
        middle = (start + end) // 2

        if self.array[middle] > self.array[end]:
            self.array[middle], self.array[end] = self.array[end], self.array[middle]

        if self.array[start] > self.array[middle]:
            self.array[start], self.array[middle] = self.array[middle], self.array[start]

        if self.array[end] > self.array[middle]:
            self.array[end], self.array[middle] = self.array[middle], self.array[end]

    # If the size of the array is less than the threshold, use insertion sort
    def quick_sort(self, start, end):
        while end - start + 1 > self.threshold:
            self.optimize_pivot(start, end)
            pivot = self.partition(start, end)

            if pivot - start < end - pivot:
                self.quick_sort(start, pivot - 1)
                start = pivot + 1
            else:
                self.quick_sort(pivot + 1, end)
                end = pivot - 1

# Quick Sort using the Dutch flag method of sorting
class QuickSortDutchFlag(QuickSort):
    def __init__(self, array):
        super().__init__(array)

    def partition(self, start, end):
        pivot = self.array[end]
        low = start - 1
        high = end
        i = start

        while i <= high:
            if self.array[i] < pivot:
                low += 1
                self.array[low], self.array[i] = self.array[i], self.array[low]
                i += 1
            elif self.array[i] > pivot:
                self.array[i], self.array[high] = self.array[high], self.array[i]
                high -= 1
            else:
                i += 1

        return low + 1, high - 1

    def quick_sort(self, start, end):
        while end - start + 1 > self.threshold:
            self.optimize_pivot(start, end)
            low, high = self.partition(start, end)

            if low - start < end - high:
                self.quick_sort(start, low - 1)
                start = high + 1
            else:
                self.quick_sort(high + 1, end)
                end = low - 1
```
## Selection Sort
```python
def selection_sort(array):
    for last in range(len(array) - 1, 0, -1):
        max_pos = 0

        for location in range(1, last + 1):
            if array[location] > array[max_pos]:
                max_pos = location

        array[max_pos], array[last] = array[last], array[max_pos]
```
## Shell Sort
```python
def gap_insertion_sort(array, start, gap):
    for i in range(start + gap, len(array), gap):
        curr_val = array[i]
        curr_pos = i

        while curr_pos >= gap and array[curr_pos - gap] > curr_val:
            array[curr_pos] = array[curr_pos - gap]
            curr_pos -= gap

        array[curr_pos] = curr_val


def shell_sort(array):
    sublist_count = len(array) // 2

    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(array, start_pos, sublist_count)

        print("After increments of size", sublist_count, "the list is", array)
        sublist_count //= 2
```
