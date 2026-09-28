import time
import tracemalloc
import sys


# --------------------------------------------------
# 1. Single Loop Traversal
# --------------------------------------------------

def single_loop(n):
    count = 0

    for i in range(n):
        count += 1

    return count


# --------------------------------------------------
# 2. Nested Loop Traversal
# --------------------------------------------------

def nested_loop(n):
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count


# --------------------------------------------------
# 3. Recursive Factorial
# --------------------------------------------------

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)


# --------------------------------------------------
# 4. Iterative Factorial
# --------------------------------------------------

def iterative_factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# --------------------------------------------------
# Benchmark Function
# --------------------------------------------------

def measure_function(function, n):

    tracemalloc.start()

    start_time = time.perf_counter()

    result = function(n)

    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_kb = peak / 1024

    return {
        "result": result,
        "time_sec": execution_time,
        "memory_kb": memory_kb
    }


# --------------------------------------------------
# Main Testing
# --------------------------------------------------

if __name__ == "__main__":

    # Allows recursive factorial to work for n = 1000
    sys.setrecursionlimit(5000)

    n = 100

    print("===== Single Loop Traversal =====")

    single_result = measure_function(single_loop, n)

    print(single_result)

    print("\n===== Nested Loop Traversal =====")

    nested_result = measure_function(nested_loop, n)

    print(nested_result)

    print("\n===== Recursive Factorial =====")

    recursive_result = measure_function(
        recursive_factorial,
        n
    )

    print(recursive_result)

    print("\n===== Iterative Factorial =====")

    iterative_result = measure_function(
        iterative_factorial,
        n
    )

    print(iterative_result)