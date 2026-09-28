# Algorithm Performance Measurement and Benchmarking Tool

A comprehensive Python benchmarking project designed to measure and compare the empirical performance of foundational searching, recursive, and iterative algorithms. This project evaluates execution time, memory overhead, number of comparisons, and operational step counts across varying dataset sizes.

---

## 📋 Table of Contents

* [Overview](https://www.google.com/search?q=%23overview&utm_source=gemini)
* [Key Features](https://www.google.com/search?q=%23key-features&utm_source=gemini)
* [Algorithms Analyzed](https://www.google.com/search?q=%23algorithms-analyzed&utm_source=gemini)
* [Project Structure](https://www.google.com/search?q=%23project-structure&utm_source=gemini)
* [Experimental Setup & Dataset Sizes](https://www.google.com/search?q=%23experimental-setup--dataset-sizes&utm_source=gemini)
* [Installation & Requirements](https://www.google.com/search?q=%23installation--requirements&utm_source=gemini)
* [Usage](https://www.google.com/search?q=%23usage&utm_source=gemini)
* [Sample Benchmark Results](https://www.google.com/search?q=%23sample-benchmark-results&utm_source=gemini)
* [Key Findings](https://www.google.com/search?q=%23key-findings&utm_source=gemini)

---

## 🔍 Overview

The main objective of this tool is to provide an empirical evaluation of algorithmic efficiency. While theoretical Big-O notation gives an asymptotic upper bound, real-world execution is influenced by Python interpreter overhead, cache behavior, call-stack memory overhead, and system load.

This project compares theoretical time/space complexity with empirical metrics using interactive tables and visual graphs (via `pandas` and `matplotlib`).

---

## ✨ Key Features

* **Multi-Metric Benchmarking:** Measures execution time (seconds), memory consumption (KB), explicit comparisons, and total operations.


* **Search Complexity Comparison:** Direct comparison between $O(N)$ Linear Search and $O(\log N)$ Binary Search.


* **Recursion vs. Iteration Analysis:** Empirical profiling of stack overhead in recursive functions versus iterative loops.


* **Traversal Complexity:** Single loop $O(N)$ vs. Nested loop $O(N^2)$ execution profiling.


* **Data Visualization:** Generates plot charts comparing input size ($N$) against execution time and resource utilization.



---

## ⚙️ Algorithms Analyzed

1. **Linear Search** – $O(N)$ Time | $O(1)$ Space


2. **Binary Search** – $O(\log N)$ Time | $O(1)$ Space


3. **Recursive Factorial** – $O(N)$ Time | $O(N)$ Call Stack Memory


4. **Iterative Factorial** – $O(N)$ Time | $O(1)$ Space


5. **Single Loop Traversal** – $O(N)$ Time


6. **Nested Loop Traversal** – $O(N^2)$ Time



---

## 📁 Project Structure

```text
├── benchmark_notebook.ipynb    # Main Google Colab / Jupyter notebook[cite: 2]
├── search_analysis.py          # Implementations for linear_search, binary_search, and measure_search[cite: 2]
├── code_benchmark.py           # Factorial, loop traversals, and function measurement wrappers[cite: 2]
├── benchmark_engine.py         # Underlying timing and memory benchmarking engine[cite: 2]
└── README.md                   # Project documentation

```

---

## 🧪 Experimental Setup & Dataset Sizes

* **Search Algorithms:** Datasets of sizes $N \in \{100, 1000, 10000, 50000\}$.


* *Worst-Case Target Selection:* Target chosen as $N-1$ (the last element) to maximize comparisons for Linear Search.




* **Recursion Limits:** Python's default recursion limit is safely extended to `5000` (`sys.setrecursionlimit(5000)`) to support factorial inputs up to $N = 1000$.



---

## 🛠️ Installation & Requirements

### Dependencies

Ensure you have Python 3.8+ installed along with the following libraries:

```bash
pip install pandas matplotlib

```

---

## 🚀 Usage

### Running in Google Colab / Jupyter Notebooks

1. Upload `search_analysis.py`, `code_benchmark.py`, and `benchmark_engine.py` to your Google Drive or root directory.


2. Open the `.ipynb` notebook and add the custom directory path if necessary:


```python
import sys
sys.path.append('/content/drive/MyDrive/Colab Notebooks')  # Update with your directory[cite: 2]

```


3. Execute the benchmarking cells:


```python
import pandas as pd
import matplotlib.pyplot as plt
from search_analysis import linear_search, binary_search, measure_search[cite: 2]
from code_benchmark import recursive_factorial, iterative_factorial, single_loop, nested_loop[cite: 2]

```



---

## 📊 Sample Benchmark Results

### Search Algorithm Comparison (Worst-Case Target $N-1$)

| Algorithm | Input Size ($N$) | Comparisons | Execution Time (sec) | Memory (KB) |
| --- | --- | --- | --- | --- |
| **Linear Search** | 100 | 100 | ~0.000033 | 0.086 |
| **Binary Search** | 100 | 7 | ~0.000007 | 0.000 |
| **Linear Search** | 1,000 | 1,000 | ~0.003993 | 0.145 |
| **Binary Search** | 1,000 | 10 | ~0.000067 | 0.156 |
| **Linear Search** | 10,000 | 10,000 | ~0.029689 | 0.145 |
| **Binary Search** | 10,000 | 14 | ~0.000091 | 0.156 |
| **Linear Search** | 50,000 | 50,000 | ~0.140519 | 0.145 |
| **Binary Search** | 50,000 | 16 | ~0.000096 | 0.156 |

(Note: Exact execution times may vary depending on system hardware, CPU load, and background processes.)

---

## 📈 Key Findings

1. **Linear vs. Binary Search:**
* Linear Search scales linearly $O(N)$ with both execution time and comparison counts.


* Binary Search scales logarithmically $O(\log N)$, taking only 16 comparisons for a dataset of 50,000 elements (compared to 50,000 comparisons in Linear Search).




2. **Execution Overhead:**
* While execution times vary slightly across runs due to operating system process scheduling, measuring exact **comparison counts** provides a stable metric to verify theoretical algorithm complexities.