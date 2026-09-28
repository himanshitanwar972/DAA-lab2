import time
import tracemalloc
import sys

from search_analysis import linear_search, binary_search
from code_benchmark import (
    single_loop,
    nested_loop,
    recursive_factorial,
    iterative_factorial
)


# Allow recursive factorial to handle n = 1000
sys.setrecursionlimit(5000)


# --------------------------------------------------
# Generic Performance Measurement
# --------------------------------------------------

def measure_function(function, *args):

    tracemalloc.start()

    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "result": result,
        "time_sec": end_time - start_time,
        "memory_kb": peak / 1024
    }


# --------------------------------------------------
# Search Benchmark
# --------------------------------------------------

def benchmark_search():

    sizes = [100, 1000, 10000, 50000]

    results = []

    for n in sizes:

        data = list(range(n))
        target = n - 1

        # Linear Search
        linear = measure_function(
            linear_search,
            data,
            target
        )

        results.append({
            "algorithm": "Linear Search",
            "input_size": n,
            "result": linear["result"][0],
            "comparisons": linear["result"][1],
            "time_sec": linear["time_sec"],
            "memory_kb": linear["memory_kb"]
        })

        # Binary Search
        binary = measure_function(
            binary_search,
            data,
            target
        )

        results.append({
            "algorithm": "Binary Search",
            "input_size": n,
            "result": binary["result"][0],
            "comparisons": binary["result"][1],
            "time_sec": binary["time_sec"],
            "memory_kb": binary["memory_kb"]
        })

    return results


# --------------------------------------------------
# Factorial Benchmark
# --------------------------------------------------

def benchmark_factorial():

    sizes = [100, 500, 1000]

    results = []

    for n in sizes:

        # Recursive Factorial
        recursive = measure_function(
            recursive_factorial,
            n
        )

        results.append({
            "algorithm": "Recursive Factorial",
            "input_size": n,
            "time_sec": recursive["time_sec"],
            "memory_kb": recursive["memory_kb"]
        })

        # Iterative Factorial
        iterative = measure_function(
            iterative_factorial,
            n
        )

        results.append({
            "algorithm": "Iterative Factorial",
            "input_size": n,
            "time_sec": iterative["time_sec"],
            "memory_kb": iterative["memory_kb"]
        })

    return results


# --------------------------------------------------
# Loop Benchmark
# --------------------------------------------------

def benchmark_loops():

    sizes = [100, 1000, 10000, 50000]

    results = []

    for n in sizes:

        # ------------------------------------------
        # Single Loop
        # ------------------------------------------

        single = measure_function(
            single_loop,
            n
        )

        results.append({
            "algorithm": "Single Loop Traversal",
            "input_size": n,
            "operations": single["result"],
            "time_sec": single["time_sec"],
            "memory_kb": single["memory_kb"]
        })

        # ------------------------------------------
        # Nested Loop
        # ------------------------------------------

        if n <= 10000:

            nested = measure_function(
                nested_loop,
                n
            )

            results.append({
                "algorithm": "Nested Loop Traversal",
                "input_size": n,
                "operations": nested["result"],
                "time_sec": nested["time_sec"],
                "memory_kb": nested["memory_kb"]
            })

        else:

            # Do not execute 50,000 x 50,000 iterations
            results.append({
                "algorithm": "Nested Loop Traversal",
                "input_size": n,
                "operations": n * n,
                "time_sec": None,
                "memory_kb": None,
                "status": "Skipped - extremely large workload"
            })

    return results


# --------------------------------------------------
# Main Program
# --------------------------------------------------

if __name__ == "__main__":

    print("\n========================================")
    print("SEARCH BENCHMARK")
    print("========================================")

    search_results = benchmark_search()

    for result in search_results:
        print(result)


    print("\n========================================")
    print("FACTORIAL BENCHMARK")
    print("========================================")

    factorial_results = benchmark_factorial()

    for result in factorial_results:
        print(result)


    print("\n========================================")
    print("LOOP BENCHMARK")
    print("========================================")

    loop_results = benchmark_loops()

    for result in loop_results:
        print(result)


    print("\n========================================")
    print("BENCHMARKING COMPLETED")
    print("========================================")