import time
import tracemalloc


def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


def measure_search(search_function, arr, target):
    tracemalloc.start()

    start_time = time.perf_counter()

    result, comparisons = search_function(arr, target)

    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_kb = peak / 1024

    return {
        "result": result,
        "comparisons": comparisons,
        "time_sec": execution_time,
        "memory_kb": memory_kb
    }


if __name__ == "__main__":

    data = list(range(1, 101))
    target = 75

    print("Linear Search")

    linear_result = measure_search(
        linear_search,
        data,
        target
    )

    print(linear_result)

    print("\nBinary Search")

    binary_result = measure_search(
        binary_search,
        data,
        target
    )

    print(binary_result)