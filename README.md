# CPU Benchmark Tool

## Overview

This tool performs a Pi calculation benchmark using the Monte Carlo simulation method. It estimates the value of Pi based on random sampling and measures the performance of the calculation over multiple iterations. The results are displayed in a graphical user interface (GUI) built with Tkinter.

## Features

- **Monte Carlo Pi Estimation**: Estimates Pi using random sampling within a unit square.
- **Benchmarking**: Runs the calculation multiple times to measure the average time taken per iteration.
- **GUI Interface**: Allows users to adjust parameters (number of samples and iterations) via sliders.
- **System Information**: Displays details about the CPU, architecture, and operating system.
- **Real-Time Results**: Displays the Pi estimates and time taken for each iteration, along with the average time for all iterations.

## Prerequisites

Before running the benchmark tool, ensure that the following libraries are installed:

- `random` (Standard Python library)
- `time` (Standard Python library)
- `platform` (Standard Python library)
- `os` (Standard Python library)
- `cpu_info` (Install via `pip install cpuinfo`)
- `tkinter` (Standard Python library for GUI)

## Installation

1. Install the `tkinter` library:

    ```bash
    pip install tk
    ```

2. Ensure you have Python 3.x and Tkinter installed.

3. Download or clone the repository containing the code.

## Usage

1. Run the Python script to start the benchmark tool.
2. The GUI will appear, where you can adjust the number of samples and iterations using the sliders.
3. Click the "Start Benchmark" button to begin the calculation.
4. The estimated value of Pi and the time taken for each iteration will be displayed in the text box.
5. The average time for all iterations will also be displayed.

### Parameters

- **Number of Samples**: The number of random points to generate for each iteration (from 100,000 to 10,000,000).
- **Number of Iterations**: The number of times to repeat the benchmark (from 1 to 100).

### Example Workflow

1. Set the "Number of Samples" to 1,000,000.
2. Set the "Number of Iterations" to 10.
3. Click "Start Benchmark."
4. View the results as Pi is estimated for each iteration, along with the time taken for each calculation.
5. After 10 iterations, the average time for all iterations will be displayed.

## System Information Displayed

The following system details are displayed at the top of the results section:

- **CPU**: The brand and model of the CPU.
- **ARCH**: The CPU architecture (e.g., x86_64).
- **OS**: The operating system running the script (e.g., Windows, Linux).

## Code Explanation

- **`monte_carlo_pi(num_samples)`**: This function runs the Monte Carlo simulation to estimate Pi by generating random points within a unit square and checking if they fall inside a unit circle.
  
- **`benchmark_pi_calculation(num_samples, num_iterations)`**: This function runs the Pi estimation multiple times and prints the result of each iteration along with the time taken.
  
- **`bench(num_samples, num_iterations)`**: This function runs the benchmark, stores the results, and updates the GUI with the system details and Pi estimates.

- **`start_benchmark()`**: This function is triggered when the "Start Benchmark" button is clicked. It reads the slider values, runs the benchmark, and displays the results.

- **GUI**: The graphical user interface is built using Tkinter, allowing users to easily interact with the tool. The results are displayed in a `Text` widget with the output formatted and centered.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
