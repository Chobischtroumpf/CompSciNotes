---
title: Chap 03 - slides_tris.pdf
authors: Alessandro Dorigo
tags: []
---

# Tri bulle
### Slide 3
```python
def bubble_sort(array):
    for end_index in range(len(array) - 1, 0, -1):
        for current in range(end_index):
            if array[current] > array[current + 1]:
                array[current], array[current + 1] = array[current + 1], array[current]
```
# Tri bulle (short)
### Slide 4
```python
def optimized_bubble_sort(array):
    swapped = True
    last_unsorted_index = len(array) - 1

    while last_unsorted_index > 0 and swapped:
        swapped = False

        for current in range(last_unsorted_index):
            if array[current] > array[current + 1]:
                swapped = True
                array[current], array[current + 1] = array[current + 1], array[current]

        last_unsorted_index -= 1
```
# Tri par selection
### Slide 6
```python
def selection_sort(array):
    for last in range(len(array) - 1, 0, -1):
        max_position = 0
        for location in range(1, last + 1):
            if array[location] > array[max_position]:
                max_position = location
        array[max_position], array[last] = array[last], array[max_position]
```
# Tri par insertion
### Slide 8
```python
def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index - 1
        while position >= 0 and array[position] > current_value:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = current_value
```
# Tri shell
### Slide 13
```python
def gap_insertion_sort(array, start, gap):
    for index in range(start + gap, len(array), gap):
        current_value = array[index]
        current_position = index

        while current_position >= gap and array[current_position - gap] > current_value:
            array[current_position] = array[current_position - gap]
            current_position -= gap

        array[current_position] = current_value
```
### Slide 14
```Python
def shell_sort(array):
    sublist_count = len(array) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(array, start_position, sublist_count)

        print("After increments of size", sublist_count, "the list is", array)
        sublist_count //= 2
```
# Merge sort
### Slide 18 et 19
```python
def merge_sort(array):
    print("Splitting", array)

    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = 0
        right_index = 0
        merged_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                array[merged_index] = left_half[left_index]
                left_index += 1
            else:
                array[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1

        while left_index < len(left_half):
            array[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_half):
            array[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

    print("Merging", array)
```
# Quicksort (v1)
### Slide 26
```python
def partition(array, start, end):
    pivot = array[end]
    smaller_element_index = start - 1

    for current_index in range(start, end):
        if array[current_index] <= pivot:
            smaller_element_index += 1
            array[smaller_element_index], array[current_index] = array[current_index], array[smaller_element_index]

    array[smaller_element_index + 1], array[end] = array[end], array[smaller_element_index + 1]
    return smaller_element_index + 1
```
### Slide 28
```python
def quick_sort(array, start, end):
    if start < end:
        partition_index = partition(array, start, end)
        quick_sort(array, start, partition_index - 1)
        quick_sort(array, partition_index + 1, end)
```
# Quicksort (v2)
### Slide 32
```python
def quick_sort_2(array, start, end):
    if start < end:
        left = start
        right = end
        pivot = array[(start + end) // 2]

        while True:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left >= right:
                break            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

        quick_sort_2(array, start, left - 1)
        quick_sort_2(array, right + 1, end)
```
# Quicksort (v3)
### Slide 32
```python
def partition_3(array, start, end):
    pivot = array[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and array[left] <= pivot:
            left += 1
        while array[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[start], array[right] = array[right], array[start]

    return right
```
### Slide 36
```python
def quickSort_3(array, start, end):
	if start < end:
		partition_index = partition_3(array, start, end)
		quickSort_3(array, start, partition_index - 1)
		quickSort_3(array, partition_index + 1, end)
```
# Quicksort (optimised)
### Slides 66, 67, 68 et 69
```python
from Insertion_Sort import insertion_sort

class QuickSort:
    def __init__(self, array):
        self.array = array
        self.threshold = 8
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

    def optimize_pivot(self, start, end):
        middle = (start + end) // 2

        if self.array[middle] > self.array[end]:
            self.array[middle], self.array[end] = self.array[end], self.array[middle]
        if self.array[start] > self.array[middle]:
            self.array[start], self.array[middle] = self.array[middle], self.array[start]
        if self.array[end] > self.array[middle]:
            self.array[end], self.array[middle] = self.array[middle], self.array[end]

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
```
