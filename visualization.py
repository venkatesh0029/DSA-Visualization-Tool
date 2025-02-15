import subprocess
import tkinter as tk
from tkinter import messagebox


def run_algorithm(algo, data):
    process = subprocess.run(
        ["java", "sort_runner" if "Sort" in algo else "search_runner", algo, data],
        capture_output=True,
        text=True,
    )
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, process.stdout)


# GUI Setup
root = tk.Tk()
root.title("DSA Visualizer")

tk.Label(root, text="Enter Numbers (comma-separated):").pack()
entry = tk.Entry(root, width=50)
entry.pack()

tk.Label(root, text="Select Algorithm:").pack()
algorithm_choice = tk.StringVar(value="BubbleSort")
options = ["BubbleSort", "QuickSort", "BinarySearch", "LinearSearch"]
dropdown = tk.OptionMenu(root, algorithm_choice, *options)
dropdown.pack()

run_button = tk.Button(
    root, text="Run", command=lambda: run_algorithm(algorithm_choice.get(), entry.get())
)
run_button.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
