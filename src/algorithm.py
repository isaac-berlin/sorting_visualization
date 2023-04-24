from random import shuffle

def bubble_sort(arr):
    """generic bubble sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list and the number of swaps performed
    """
    nunmber_of_swaps = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                nunmber_of_swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, nunmber_of_swaps


def selection_sort(arr):
    """generic selection sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list and the number of swaps performed
    """
    number_of_swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        number_of_swaps += 1
    return arr, number_of_swaps


def insertion_sort(arr):
    """generic insertion sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list and the number of swaps performed
    """
    number_of_swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            number_of_swaps += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr, number_of_swaps


def merge_sort(arr):
    """generic merge sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list and the number of swaps performed
    """
    number_of_swaps = 0
    right_swaps = 0
    left_swaps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left_swaps = merge_sort(left)[1]
        right_swaps = merge_sort(right)[1]
        i = j = k = 0
        while i < len(left) and j < len(right):
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
    return arr, (number_of_swaps+left_swaps+right_swaps)

def bogo_sort(arr):
    """generic bogo sort algorithm

    Args:
        arr (list): list of integers to be sorted

    Returns:
        tuple: a tuple containing a sorted list and the number of swaps performed
    """
    number_of_swaps = 0
    while not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        shuffle(arr)
        number_of_swaps += 1
    return arr, number_of_swaps
