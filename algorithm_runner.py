import subprocess


def run_algorithm(algorithm, data):
    cmd = [
        "java",
        "sort_runner" if "Sort" in algorithm else "search_runner",
        algorithm,
        data,
    ]
    process = subprocess.run(cmd, capture_output=True, text=True)
    return process.stdout


if __name__ == "__main__":
    algo = input("Enter Algorithm (BubbleSort/QuickSort/BinarySearch/LinearSearch): ")
    data = input("Enter numbers (comma-separated): ")
    result = run_algorithm(algo, data)
    print(result)
