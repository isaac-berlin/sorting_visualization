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

def main():
    # store results in a dictionary
    results = {}

    # bubble_sort
    results["bubble_sort"] = {}
    
    # test 100 random arrays of size 100
    arrs = [[randint(0, 100) for i in range(100)] for j in range(100)]
    time, swaps = test_avg(bubble_sort, arrs)
    results["bubble_sort"][100] = {"time": time, "swaps": swaps}
    
    # test 100 random arrays of size 10,000
    # arrs = [[randint(0, 100) for i in range(10_000)] for j in range(100)]
    # time, swaps = test_avg(bubble_sort, arrs)
    results["bubble_sort"][10_000] = {"time": time, "swaps": swaps}
    
    
    # selection_sort
    results["selection_sort"] = {}
    
    # test 100 random arrays of size 100
    arrs = [[randint(0, 100) for i in range(100)] for j in range(100)]
    time, swaps = test_avg(selection_sort, arrs)
    results["selection_sort"][100] = {"time": time, "swaps": swaps}
    
    # test 100 random arrays of size 10,000
    # arrs = [[randint(0, 100) for i in range(10_000)] for j in range(100)]
    # time, swaps = test_avg(selection_sort, arrs)
    results["selection_sort"][10_000] = {"time": time, "swaps": swaps}
    
    
    # insertion_sort
    results["insertion_sort"] = {}
    
    # test 100 random arrays of size 100
    arrs = [[randint(0, 100) for i in range(100)] for j in range(100)]
    time, swaps = test_avg(insertion_sort, arrs)
    results["insertion_sort"][100] = {"time": time, "swaps": swaps}
    
    # test 100 random arrays of size 10,000
    # arrs = [[randint(0, 100) for i in range(10_000)] for j in range(100)]
    # time, swaps = test_avg(insertion_sort, arrs)
    results["insertion_sort"][10_000] = {"time": time, "swaps": swaps}
    
    
    # merge_sort
    results["merge_sort"] = {}

    # test 100 random arrays of size 100
    arrs = [[randint(0, 100) for i in range(100)] for j in range(100)]
    time, swaps = test_avg(merge_sort, arrs)
    results["merge_sort"][100] = {"time": time, "swaps": swaps}
    
    # test 100 random arrays of size 10,000
    # arrs = [[randint(0, 100) for i in range(10_000)] for j in range(100)]
    # time, swaps = test_avg(merge_sort, arrs)
    results["merge_sort"][10_000] = {"time": time, "swaps": swaps}
    
    bubble = [results["bubble_sort"][100]["swaps"], results["bubble_sort"][10_000]["swaps"]]
    selection = [results["selection_sort"][100]["swaps"], results["selection_sort"][10_000]["swaps"]]
    insertion = [results["insertion_sort"][100]["swaps"], results["insertion_sort"][10_000]["swaps"]]
    merge = [results["merge_sort"][100]["swaps"], results["merge_sort"][10_000]["swaps"]]
    
    df = pd.DataFrame({"Bubble Sort": bubble, "Selection Sort": selection, "Insertion Sort": insertion, "Merge Sort": merge}, index=[100, 10_000])
    df.plot(kind="bar", title="Swaps", figsize=(10, 5), subplots=True, layout=(2, 2), xlabel="Array Size", ylabel="Swaps")
    plt.show()
    
    print(bubble)
    print(selection)
    print(insertion)
    print(merge)
    
    
    print(results)
    
if __name__ == "__main__":
    main()