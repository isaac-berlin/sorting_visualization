from random import shuffle

def bubble_sort(arr):
    """generic bubble sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list, the number of swaps performed, and number of comparisons performed
    """
    nunmber_of_swaps = 0
    nunmber_of_comparisons = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            nunmber_of_comparisons += 1
            if arr[j] > arr[j + 1]:
                nunmber_of_swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, nunmber_of_swaps, nunmber_of_comparisons


def selection_sort(arr):
    """generic selection sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list, the number of swaps performed, and number of comparisons performed
    """
    number_of_swaps = 0
    number_of_comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            number_of_comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            number_of_swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, number_of_swaps, number_of_comparisons


def insertion_sort(arr):
    """generic insertion sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list, the number of swaps performed, and number of comparisons performed
    """
    number_of_swaps = 0
    number_of_comparisons = 0
    for i in range(1, len(arr)):
        j = i 
        while j > 0 and arr[j] < arr[j-1]:
            number_of_comparisons += 1
            number_of_swaps += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr, number_of_swaps, number_of_comparisons


def merge_sort(arr):
    """generic merge sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list, the number of swaps performed, and number of comparisons performed
    """
    number_of_swaps = 0
    number_of_comparisons = 0
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left_results = merge_sort(left)
        right_results = merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            number_of_comparisons += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            number_of_swaps += 1
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            number_of_swaps += 1
            arr[k] = right[j]
            j += 1
            k += 1
    return arr, (number_of_swaps+left_results[1]+right_results[1]), (number_of_comparisons+left_results[2]+right_results[2])

def bogo_sort(arr):
    """generic bogo sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list, the number of swaps performed, and number of comparisons performed
    """
    number_of_swaps = 0
    number_of_comparisons = 0
    while not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        shuffle(arr)
        number_of_swaps += 1
        number_of_comparisons += 1
    return arr, number_of_swaps, number_of_comparisons


lst = [2, 8, 5, 3, 9, 4]
sorted = insertion_sort(lst)
print(sorted)