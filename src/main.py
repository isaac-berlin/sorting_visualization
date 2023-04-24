import matplotlib.pyplot as plt
from random import randint
from time import perf_counter
from algorithm import bubble_sort, selection_sort, insertion_sort, merge_sort
import pandas as pd

def test_avg(algorithm, arrs):
    """
    Executes the specified algorithm on multiple arrays and measures the execution time and number of swaps performed. Returns the average execution time and number of swaps performed.

    Args:
        algorithm (_type_): A function that takes an array as an argument and returns a tuple containing a sorted array and the number of swaps performed.
        arrs (_type_): A list of arrays to be sorted.

    Returns:
        tuple: a tuple containing the average execution time and average number of swaps performed.
    """
    time, swaps = test(algorithm, arrs)   
    avg_time = sum(time) / len(time)
    avg_swaps = sum(swaps) / len(swaps)
    return avg_time, avg_swaps

def test(algorithm, arrs):
    """
    Executes the specified algorithm on multiple arrays and measures the execution time and number of swaps performed.

    Args:
        algorithm (function): A function that takes an array as an argument and returns a tuple containing a sorted array and the number of swaps performed.
        arrs (list): A list of arrays to be sorted.

    Returns:
        tuple: A tuple containing two lists. The first list contains the execution time for each array in seconds, and the second list contains the number of swaps performed for each array.
    """
    tiks, toks, swaps = [], [], []
    for arr in arrs:
        tiks.append(perf_counter())
        swaps.append(algorithm(arr)[1])
        toks.append(perf_counter())
        
    time = [toks[i] - tiks[i] for i in range(len(tiks))]
    return time, swaps

def make_list(start: int, stop: int) -> list:
    """Generates a list of lists of random integers. Each sublist has a size between in the range [start, stop). Each integer in the sublists is in the range [0, 100].

    Args:
        start (int): size of the smallest sublist (inclusive)
        stop (int): size of the largest sublist (exclusive)

    Returns:
        list: list of lists of random integers
    """
    lst = []
    for i in range(start, stop):
        sublst = [randint(0,100) for j in range(i)]
        lst.append(sublst)
    return lst


def main():
    MIN_SIZE = 10
    MAX_SIZE = 1000
    
    lst = make_list(MIN_SIZE, MAX_SIZE)    
    bubble_time, bubble_swaps = test(bubble_sort, lst)
    
    lst = make_list(MIN_SIZE, MAX_SIZE) 
    selection_time, selection_swaps = test(selection_sort, lst)
    
    lst = make_list(MIN_SIZE, MAX_SIZE) 
    insertion_time, insertion_swaps = test(insertion_sort, lst)
    
    lst = make_list(MIN_SIZE, MAX_SIZE) 
    merge_time, merge_swaps = test(merge_sort, lst)
    
    plt.plot(bubble_time, label="Bubble Sort")
    plt.plot(selection_time, label="Selection Sort")
    plt.plot(insertion_time, label="Insertion Sort")
    plt.plot(merge_time, label="Merge Sort")
    
    plt.xlabel("Size of array")
    plt.ylabel("Time (s)")
    plt.title("Time Complexity of Sorting Algorithms")
    plt.legend()
    plt.show()
    
    
if __name__ == "__main__":
    main()