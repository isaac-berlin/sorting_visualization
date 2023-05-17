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
    
    def merge(left_arr, right_arr):
        """gereic merge function for merge sort

        Args:
            left_arr (list): left array to be merged
            right_arr (list): right array to be merged
        """
        nonlocal number_of_swaps
        nonlocal number_of_comparisons
        merged_arr = []
        
        while len(left_arr) > 0 and len(right_arr) > 0:
            number_of_comparisons += 1
            if left_arr[0] < right_arr[0]:
                number_of_swaps += 1
                merged_arr.append(left_arr.pop(0))
            else:
                merged_arr.append(right_arr.pop(0))
        
        while len(left_arr) > 0:
            merged_arr.append(left_arr.pop(0))
            
        while len(right_arr) > 0:
            merged_arr.append(right_arr.pop(0))
            
        return merged_arr
    
    if len(arr) == 1:
         return arr, number_of_swaps, number_of_comparisons 

    left_arr, left_swaps, left_comparisons = merge_sort(arr[:len(arr) // 2])
    right_arr, right_swaps, right_comparisons = merge_sort(arr[len(arr) // 2:])
    
    return merge(left_arr, right_arr), number_of_swaps, number_of_comparisons

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