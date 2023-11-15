import random
import time
import platform
import os
import cpu_info
import tkinter as tk

# Default parameters
num_samples = 1000000
num_iterations = 10

# Function to estimate Pi using Monte Carlo simulation
def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

# Function to run Pi calculation benchmark
def benchmark_pi_calculation(num_samples, num_iterations):
    total_time = 0
    for _ in range(num_iterations):
        start_time = time.time()
        pi_estimate = monte_carlo_pi(num_samples)
        end_time = time.time()
        total_time += end_time - start_time
        print(f"Iteration {_:2}: π ≈ {pi_estimate:.8f} (Time: {end_time - start_time:.4f} seconds)")

    average_time = total_time / num_iterations
    print(f"Average Time for {num_iterations} iterations: {average_time:.4f} seconds")

# Function to perform the benchmark and display results in the GUI
def bench(num_samples, num_iterations):
    os.system("cls")  # Clear the console

    results = []
    for _ in range(num_iterations):
        start_time = time.time()
        pi_estimate = monte_carlo_pi(num_samples)
        end_time = time.time()
        duration = end_time - start_time
        results.append((start_time, end_time, duration, pi_estimate))

    average_time = sum(duration for _, _, duration, _ in results) / (num_iterations - 1)

    # Clear previous results in the GUI text widget
    results_text.delete(1.0, tk.END)

    # Display system information and results in the GUI
    details = f"""
        CPU: {cpu_info.get_cpu_info().get('brand_raw', "Unknown")}
        ARCH: {cpu_info.get_cpu_info().get('arch_string_raw', "Unknown")}
        OS: {str(platform.system())}

        Num Samples: {num_samples}
        Num Iterations: {num_iterations}
    """
    results_text.insert(tk.END, details + "\n\n", "center")

    for i, (start_time, end_time, duration, pi_estimate) in enumerate(results, 1):
        results_text.insert(tk.END, f"Iteration {i}: π ≈ {pi_estimate:.8f} (Time: {duration:.4f} seconds)\n", "center")
    results_text.insert(tk.END, f"\nAverage Time for {num_iterations} iterations: {average_time:.4f} seconds\n", "center")

# Function to start the benchmark when the button is clicked
def start_benchmark():
    global num_samples, num_iterations
    num_samples = int(samples_slider.get())
    num_iterations = int(iterations_slider.get())
    bench(num_samples, num_iterations)

# Create a tkinter window
root = tk.Tk()
root.title("CPU Benchmark Tool")
root.state("zoomed")  # Maximize the window

# Create and configure sliders for samples and iterations
samples_slider = tk.Scale(root, from_=100000, to=10000000, orient="horizontal", label="No. of Samples")
samples_slider.set(num_samples)
iterations_slider = tk.Scale(root, from_=1, to=100, orient="horizontal", label="No. of Iterations")
iterations_slider.set(num_iterations)

# Create a button to start the benchmark
start_button = tk.Button(root, text="Start Benchmark", command=start_benchmark)

# Create a text widget for displaying results
font = ("Helvetica", 16)
results_text = tk.Text(root, wrap=tk.WORD, height=25, width=80, font=font)
results_text.tag_configure("center", justify="center")
results_text.insert(tk.END, "Results will be displayed here.", "center")

# Pack the widgets
samples_slider.pack()
iterations_slider.pack()
start_button.pack()
results_text.pack()

# Start the GUI main loop
root.mainloop()
