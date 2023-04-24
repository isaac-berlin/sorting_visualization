import matplotlib.pyplot as plt
from random import randint
from time import perf_counter
from algorithm import bubble_sort, selection_sort, insertion_sort, merge_sort
import pandas as pd

def test_avg(algorithm, arrs):
    time, swaps = test(algorithm, arrs)   
    avg_time = sum(time) / len(time)
    avg_swaps = sum(swaps) / len(swaps)
    return avg_time, avg_swaps

def test(algorithm, arrs):
    tiks, toks, swaps = [], [], []
    for arr in arrs:
        tiks.append(perf_counter())
        swaps.append(algorithm(arr)[1])
        toks.append(perf_counter())
        
    time = [toks[i] - tiks[i] for i in range(len(tiks))]
    return time, swaps

def make_list(start, stop):
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