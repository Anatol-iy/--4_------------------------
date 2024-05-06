import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    return sorted(arr)

random_data = [random.randint(0, 1000) for _ in range(1000)]

# Відсортований за зростанням
sorted_data = sorted(random_data)

# Відсортований за спаданням
reversed_data = sorted(random_data, reverse=True)

# Проведемо замір часу виконання для кожного алгоритму на різних наборах даних
merge_sort_time_random = timeit.timeit(lambda: merge_sort(random_data), number=100)
merge_sort_time_sorted = timeit.timeit(lambda: merge_sort(sorted_data), number=100)
merge_sort_time_reversed = timeit.timeit(lambda: merge_sort(reversed_data), number=100)

insertion_sort_time_random = timeit.timeit(lambda: insertion_sort(random_data), number=100)
insertion_sort_time_sorted = timeit.timeit(lambda: insertion_sort(sorted_data), number=100)
insertion_sort_time_reversed = timeit.timeit(lambda: insertion_sort(reversed_data), number=100)

timsort_time_random = timeit.timeit(lambda: timsort(random_data), number=100)
timsort_time_sorted = timeit.timeit(lambda: timsort(sorted_data), number=100)
timsort_time_reversed = timeit.timeit(lambda: timsort(reversed_data), number=100)

# Виведемо результати
print("Merge Sort:")
print("Random Data:", merge_sort_time_random)
print("Sorted Data:", merge_sort_time_sorted)
print("Reversed Data:", merge_sort_time_reversed)

print("\nInsertion Sort:")
print("Random Data:", insertion_sort_time_random)
print("Sorted Data:", insertion_sort_time_sorted)
print("Reversed Data:", insertion_sort_time_reversed)

print("\nTimsort:")
print("Random Data:", timsort_time_random)
print("Sorted Data:", timsort_time_sorted)
print("Reversed Data:", timsort_time_reversed)