import random
import time
import sys
import matplotlib.pyplot as plt

# Increase recursion limit
sys.setrecursionlimit(20000)


# --------------------------
# Quicksort Implementations
# --------------------------

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def three_way_quicksort(arr, low, high):
    if low >= high:
        return

    lt = low
    gt = high
    pivot = arr[low]
    i = low + 1

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    three_way_quicksort(arr, low, lt - 1)
    three_way_quicksort(arr, gt + 1, high)


# --------------------------
# Array Generators
# --------------------------

def generate_random_array(size, value_range=(0, 10000)):
    return [random.randint(*value_range) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(size))


def generate_reverse_sorted_array(size):
    return list(range(size - 1, -1, -1))


def generate_repeated_elements_array(size, repeated_value=5):
    return [repeated_value] * size


def time_sort(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_func(arr_copy, 0, len(arr_copy) - 1)
    end = time.perf_counter()
    assert arr_copy == sorted(arr), "Sorting failed!"
    return end - start


def benchmark_and_plot():
    sizes = [1000, 5000, 10000]
    input_types = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array,
        "Repeated Elements": generate_repeated_elements_array
    }

    for input_name, generator in input_types.items():
        rand_times = []
        det_times = []

        print(f"\nBenchmarking for: {input_name} array")
        for size in sizes:
            arr = generator(size)
            print(f"  Size: {size}")

            t_rand = time_sort(randomized_quicksort, arr)
            t_det = time_sort(three_way_quicksort, arr)

            rand_times.append(t_rand)
            det_times.append(t_det)

            print(f"    Randomized: {t_rand:.6f}s, Deterministic (3-way): {t_det:.6f}s")

        # Plot for current input type
        plt.figure(figsize=(8, 5))
        bar_width = 0.35
        indices = range(len(sizes))

        plt.bar([i - bar_width / 2 for i in indices], rand_times, width=bar_width, label='Randomized')
        plt.bar([i + bar_width / 2 for i in indices], det_times, width=bar_width, label='Deterministic (3-way)')

        plt.xticks(indices, [str(size) for size in sizes])
        plt.xlabel("Array Size")
        plt.ylabel("Time (seconds)")
        plt.title(f"Quicksort Performance - {input_name} Array")
        plt.legend()
        plt.tight_layout()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()



if __name__ == "__main__":
    benchmark_and_plot()
