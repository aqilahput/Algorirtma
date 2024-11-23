#MERGE_SORT(arr)
#If length of arr <= 1
#return arr
#Split arr into two halves: left and right
#Call MERGE_SORT(left)
#Call MERGE_SORT(right)
#Merge the sorted left and right into sorted_array
#Return sorted_array

#BUBBLE_SORT(arr)
#For i from 0 to length of arr - 1
#For j from 0 to length of arr - i - 1
#If arr[j] > arr[j + 1]
#Swap arr[j] and arr[j + 1]
#Return arr

#Program
import time
import random

# Implementasi Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

# Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Generate random integers
X = [random.randint(0, 1000) for _ in range(100)]

# Measure time for Merge Sort
start_time = time.time()
merge_sorted = merge_sort(X.copy())
merge_sort_time = time.time() - start_time

# Measure time for Bubble Sort
start_time = time.time()
bubble_sorted = bubble_sort(X.copy())
bubble_sort_time = time.time() - start_time

# Output Results
print("Original Array:", X)
print("\nSorted with Merge Sort:", merge_sorted)
print("Merge Sort Time:", merge_sort_time, "seconds")
print("\nSorted with Bubble Sort:", bubble_sorted)
print("Bubble Sort Time:", bubble_sort_time, "seconds")

#Analisa Kompleksitas

#Merge Sort:
#Best Case, Average Case, Worst Case: O(n log n)
#Space Complexity: O(n) (Membutuhkan array tambahan saat proses merging)

#Bubble Sort:
#Best Case: O(n) (Jika array sudah terurut)
#Average Case, Worst Case: O(n²)
#Space Complexity: O(1) (In-place sorting)


