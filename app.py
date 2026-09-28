import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from search_analysis import (
    linear_search,
    binary_search,
    measure_search
)

from code_benchmark import (
    single_loop,
    nested_loop,
    recursive_factorial,
    iterative_factorial,
    measure_function
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Algorithm Performance Tool",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 Algorithm Performance Measurement Tool")

st.write(
    "Analyze algorithm execution time, memory usage, "
    "comparisons, and performance as input size increases."
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Algorithm Selection")

category = st.sidebar.selectbox(
    "Select Category",
    [
        "Search Algorithms",
        "Factorial Algorithms",
        "Loop Algorithms"
    ]
)


# ==================================================
# SEARCH ALGORITHMS
# ==================================================

if category == "Search Algorithms":

    st.header("🔍 Search Algorithm Analysis")

    algorithm = st.selectbox(
        "Select Search Algorithm",
        [
            "Linear Search",
            "Binary Search"
        ]
    )

    input_size = st.number_input(
        "Enter Dataset Size",
        min_value=1,
        max_value=50000,
        value=1000,
        step=100
    )

    target = st.number_input(
        "Enter Search Key",
        min_value=0,
        value=input_size - 1,
        step=1
    )

    if st.button("Run Search"):

        data = list(range(int(input_size)))

        if target >= input_size:
            st.error("Search key must be smaller than dataset size.")

        else:

            if algorithm == "Linear Search":

                result = measure_search(
                    linear_search,
                    data,
                    int(target)
                )

            else:

                result = measure_search(
                    binary_search,
                    data,
                    int(target)
                )

            st.subheader("Search Results")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Result Index",
                result["result"]
            )

            col2.metric(
                "Comparisons",
                result["comparisons"]
            )

            col3.metric(
                "Execution Time",
                f"{result['time_sec']:.8f} sec"
            )

            col4.metric(
                "Memory Usage",
                f"{result['memory_kb']:.4f} KB"
            )


# ==================================================
# FACTORIAL ALGORITHMS
# ==================================================

elif category == "Factorial Algorithms":

    st.header("🔢 Factorial Algorithm Analysis")

    algorithm = st.selectbox(
        "Select Factorial Algorithm",
        [
            "Recursive Factorial",
            "Iterative Factorial"
        ]
    )

    input_size = st.number_input(
        "Enter Factorial Input",
        min_value=1,
        max_value=1000,
        value=100,
        step=100
    )

    if st.button("Run Factorial"):

        if algorithm == "Recursive Factorial":

            result = measure_function(
                recursive_factorial,
                int(input_size)
            )

        else:

            result = measure_function(
                iterative_factorial,
                int(input_size)
            )

        st.subheader("Factorial Results")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Input Size",
            input_size
        )

        col2.metric(
            "Execution Time",
            f"{result['time_sec']:.8f} sec"
        )

        col3.metric(
            "Memory Usage",
            f"{result['memory_kb']:.4f} KB"
        )

        st.write("Factorial calculated successfully.")


# ==================================================
# LOOP ALGORITHMS
# ==================================================

else:

    st.header("🔄 Loop Algorithm Analysis")

    algorithm = st.selectbox(
        "Select Loop Algorithm",
        [
            "Single Loop Traversal",
            "Nested Loop Traversal"
        ]
    )

    input_size = st.number_input(
        "Enter Number of Iterations",
        min_value=1,
        max_value=10000,
        value=100,
        step=100
    )

    if st.button("Run Loop"):

        if algorithm == "Single Loop Traversal":

            result = measure_function(
                single_loop,
                int(input_size)
            )

        else:

            # Prevent extremely large nested-loop workloads
            if input_size > 10000:

                st.warning(
                    "Nested loops above 10,000 are disabled "
                    "because they require an extremely large "
                    "number of iterations."
                )

                st.stop()

            result = measure_function(
                nested_loop,
                int(input_size)
            )

        st.subheader("Loop Results")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Operations",
            result["result"]
        )

        col2.metric(
            "Execution Time",
            f"{result['time_sec']:.8f} sec"
        )

        col3.metric(
            "Memory Usage",
            f"{result['memory_kb']:.4f} KB"
        )


# --------------------------------------------------
# Complexity Table
# --------------------------------------------------

st.sidebar.markdown("---")

st.sidebar.subheader("Time & Space Complexity")

complexity_data = {
    "Algorithm": [
        "Linear Search",
        "Binary Search",
        "Recursive Factorial",
        "Iterative Factorial",
        "Single Loop Traversal",
        "Nested Loop Traversal"
    ],

    "Time Complexity": [
        "O(n)",
        "O(log n)",
        "O(n)",
        "O(n)",
        "O(n)",
        "O(n²)"
    ],

    "Space Complexity": [
        "O(1)",
        "O(1)",
        "O(n)",
        "O(1)",
        "O(1)",
        "O(1)"
    ]
}

complexity_df = pd.DataFrame(complexity_data)

with st.expander("View Complexity Table"):

    st.dataframe(
        complexity_df,
        use_container_width=True
    )

# ==================================================
# AUTOMATED BENCHMARKING & VISUALIZATION
# ==================================================

st.sidebar.markdown("---")

st.sidebar.subheader("Automated Benchmarking")

if st.sidebar.button("Run All Benchmarks"):

    st.header("📈 Automated Benchmark Results")

    # --------------------------------------------------
    # SEARCH BENCHMARK
    # --------------------------------------------------

    st.subheader("🔍 Search Algorithm Benchmark")

    search_sizes = [100, 1000, 10000, 50000]

    search_data = []

    for n in search_sizes:

        data = list(range(n))
        target = n - 1

        # Linear Search
        linear = measure_search(
            linear_search,
            data,
            target
        )

        search_data.append({
            "Algorithm": "Linear Search",
            "Input Size": n,
            "Comparisons": linear["comparisons"],
            "Execution Time": linear["time_sec"],
            "Memory (KB)": linear["memory_kb"]
        })

        # Binary Search
        binary = measure_search(
            binary_search,
            data,
            target
        )

        search_data.append({
            "Algorithm": "Binary Search",
            "Input Size": n,
            "Comparisons": binary["comparisons"],
            "Execution Time": binary["time_sec"],
            "Memory (KB)": binary["memory_kb"]
        })

    search_df = pd.DataFrame(search_data)

    st.dataframe(
        search_df,
        use_container_width=True
    )

    # Search Graph

    fig, ax = plt.subplots()

    for algorithm in ["Linear Search", "Binary Search"]:

        data = search_df[
            search_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Execution Time"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Dataset Size")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Linear Search vs Binary Search")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # --------------------------------------------------
    # FACTORIAL BENCHMARK
    # --------------------------------------------------

    st.subheader("🔢 Factorial Algorithm Benchmark")

    factorial_sizes = [100, 500, 1000]

    factorial_data = []

    for n in factorial_sizes:

        # Recursive
        recursive = measure_function(
            recursive_factorial,
            n
        )

        factorial_data.append({
            "Algorithm": "Recursive Factorial",
            "Input Size": n,
            "Execution Time": recursive["time_sec"],
            "Memory (KB)": recursive["memory_kb"]
        })

        # Iterative
        iterative = measure_function(
            iterative_factorial,
            n
        )

        factorial_data.append({
            "Algorithm": "Iterative Factorial",
            "Input Size": n,
            "Execution Time": iterative["time_sec"],
            "Memory (KB)": iterative["memory_kb"]
        })

    factorial_df = pd.DataFrame(factorial_data)

    st.dataframe(
        factorial_df,
        use_container_width=True
    )

    # Factorial Graph

    fig, ax = plt.subplots()

    for algorithm in [
        "Recursive Factorial",
        "Iterative Factorial"
    ]:

        data = factorial_df[
            factorial_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Execution Time"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Recursive vs Iterative Factorial")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # --------------------------------------------------
    # LOOP BENCHMARK
    # --------------------------------------------------

    st.subheader("🔄 Loop Algorithm Benchmark")

    loop_sizes = [100, 1000, 10000]

    loop_data = []

    for n in loop_sizes:

        # Single Loop
        single = measure_function(
            single_loop,
            n
        )

        loop_data.append({
            "Algorithm": "Single Loop Traversal",
            "Input Size": n,
            "Operations": single["result"],
            "Execution Time": single["time_sec"],
            "Memory (KB)": single["memory_kb"]
        })

        # Nested Loop
        nested = measure_function(
            nested_loop,
            n
        )

        loop_data.append({
            "Algorithm": "Nested Loop Traversal",
            "Input Size": n,
            "Operations": nested["result"],
            "Execution Time": nested["time_sec"],
            "Memory (KB)": nested["memory_kb"]
        })

    loop_df = pd.DataFrame(loop_data)

    st.dataframe(
        loop_df,
        use_container_width=True
    )

    # Loop Graph

    fig, ax = plt.subplots()

    for algorithm in [
        "Single Loop Traversal",
        "Nested Loop Traversal"
    ]:

        data = loop_df[
            loop_df["Algorithm"] == algorithm
        ]

        ax.plot(
            data["Input Size"],
            data["Execution Time"],
            marker="o",
            label=algorithm
        )

    ax.set_xlabel("Number of Iterations")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Single Loop vs Nested Loop")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.success("All benchmarks completed successfully.")

# ==================================================
# COMPARATIVE STUDY
# ==================================================

st.sidebar.markdown("---")

st.sidebar.subheader("Comparative Study")

if st.sidebar.button("Show Comparative Study"):

    st.header("📊 Comparative Study")

    # --------------------------------------------------
    # Search Comparison
    # --------------------------------------------------

    st.subheader("1. Linear Search vs Binary Search")

    st.write(
        """
        Linear Search checks elements sequentially from the beginning
        of the dataset. Binary Search repeatedly divides the sorted
        dataset into smaller parts.
        """
    )

    search_comparison = pd.DataFrame({
        "Algorithm": [
            "Linear Search",
            "Binary Search"
        ],
        "Time Complexity": [
            "O(n)",
            "O(log n)"
        ],
        "Space Complexity": [
            "O(1)",
            "O(1)"
        ],
        "Main Characteristic": [
            "Checks elements sequentially",
            "Divides the search range repeatedly"
        ]
    })

    st.dataframe(
        search_comparison,
        use_container_width=True
    )

    st.write(
        """
        As the dataset size increases, the number of comparisons
        performed by Linear Search increases approximately linearly.
        Binary Search requires substantially fewer comparisons because
        it eliminates approximately half of the remaining search space
        at each step.
        """
    )

    # --------------------------------------------------
    # Factorial Comparison
    # --------------------------------------------------

    st.subheader("2. Recursive Factorial vs Iterative Factorial")

    factorial_comparison = pd.DataFrame({
        "Algorithm": [
            "Recursive Factorial",
            "Iterative Factorial"
        ],
        "Time Complexity": [
            "O(n)",
            "O(n)"
        ],
        "Space Complexity": [
            "O(n)",
            "O(1)"
        ],
        "Implementation": [
            "Uses recursive function calls",
            "Uses a loop"
        ]
    })

    st.dataframe(
        factorial_comparison,
        use_container_width=True
    )

    st.write(
        """
        Both factorial implementations perform O(n) work.
        However, the recursive implementation requires additional
        call-stack space for recursive calls, while the iterative
        implementation maintains constant auxiliary space.
        """
    )

    # --------------------------------------------------
    # Loop Comparison
    # --------------------------------------------------

    st.subheader("3. Single Loop vs Nested Loop")

    loop_comparison = pd.DataFrame({
        "Algorithm": [
            "Single Loop Traversal",
            "Nested Loop Traversal"
        ],
        "Time Complexity": [
            "O(n)",
            "O(n²)"
        ],
        "Space Complexity": [
            "O(1)",
            "O(1)"
        ],
        "Operations": [
            "Approximately n",
            "Approximately n²"
        ]
    })

    st.dataframe(
        loop_comparison,
        use_container_width=True
    )

    st.write(
        """
        A single loop performs approximately n operations.
        A nested loop performs approximately n × n operations.
        Therefore, increasing the input size has a much larger effect
        on the nested-loop execution time.
        """
    )

    # --------------------------------------------------
    # Input Size Impact
    # --------------------------------------------------

    st.subheader("4. Impact of Input Size")

    input_effect = pd.DataFrame({
        "Algorithm": [
            "Linear Search",
            "Binary Search",
            "Recursive Factorial",
            "Iterative Factorial",
            "Single Loop",
            "Nested Loop"
        ],
        "Effect of Increasing Input": [
            "Execution time increases approximately linearly",
            "Execution time grows much more slowly",
            "Execution time increases with n",
            "Execution time increases with n",
            "Execution time increases approximately linearly",
            "Execution time increases approximately quadratically"
        ]
    })

    st.dataframe(
        input_effect,
        use_container_width=True
    )

    # --------------------------------------------------
    # Time-Space Trade-Off
    # --------------------------------------------------

    st.subheader("5. Time-Space Trade-Off")

    st.write(
        """
        Algorithm performance depends on both execution time and
        memory usage. Recursive Factorial uses additional call-stack
        memory because each recursive call remains active until the
        base case is reached. Iterative Factorial avoids this recursive
        call stack and therefore has constant auxiliary space.
        """
    )

    # --------------------------------------------------
    # Conclusion
    # --------------------------------------------------

    st.subheader("6. Comparative Conclusion")

    st.write(
        """
        The experimental results demonstrate that algorithmic
        complexity strongly influences performance as input size
        increases. Linear Search and Single Loop Traversal scale
        approximately linearly, while Binary Search reduces the
        number of search comparisons logarithmically. Both factorial
        implementations have linear time complexity, while the
        recursive implementation requires additional stack space.
        Nested Loop Traversal has quadratic time complexity and its
        workload increases much more rapidly as the input size grows.
        """
    )

    st.success("Comparative study displayed successfully.")