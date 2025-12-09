import importlib
import os
import sys
import time
import tracemalloc
from colorama import Fore, Style

BRIGHT_GREEN = "\033[32m"
RESET = "\033[0m"

def get_input_file(day: str, test: bool = False) -> str:
    return (
        os.path.join(day, "test_input.txt")
        if test
        else os.path.join(day, "input.txt")
    )

def run_solution(day, test: bool = False, part: int = None, benchmark: bool = False, iterations: int = 10):
    day_folder = f"days/{day}"
    solution_file = os.path.join(day_folder, "solution.py")
    input_file = get_input_file(day_folder, test)

    if not os.path.exists(solution_file):
        print(f"Solution for Day {day} not found!")
        return

    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found!")
        return

    # Dynamically add the day folder to sys.path
    sys.path.insert(0, os.path.abspath(day_folder))

    # Dynamically import the solution module
    module_name = f"days.{day}.solution"
    try:
        solution = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Could not import solution for Day {day}: {e}")
        return

    with open(input_file) as f:
        data = f.read()

    if benchmark:
        run_benchmark(solution, data, test, day, part, iterations)
    else:
        print(f"Running Day {day}...")
        def run(partNo: int):
            start = time.time()
            if partNo == 1:
                print("Part 1:", f"{BRIGHT_GREEN}{solution.part1(data, test)}{RESET}", end=' ')
            elif partNo == 2:
                print("Part 2:", f"{BRIGHT_GREEN}{solution.part2(data, test)}{RESET}", end=' ')
            elapsed = time.time() - start
            print(Fore.YELLOW + f"{elapsed:.6f} seconds" + Style.RESET_ALL)

        [run(partNo) for partNo in [1,2] if part is None or part == partNo]


def run_benchmark(solution, data, test, day, part, iterations):
    print(f"Benchmarking 2025: day {day}")
    total_start = time.time()

    parts_to_run = [1, 2] if part is None else [part]

    for partNo in parts_to_run:
        func = solution.part1 if partNo == 1 else solution.part2
        times = []

        # Warmup run
        func(data, test)

        # Measure memory separately (single run to avoid overhead)
        tracemalloc.start()
        func(data, test)
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Time without tracemalloc overhead
        for _ in range(iterations):
            start = time.time()
            func(data, test)
            elapsed = time.time() - start
            times.append(elapsed)

        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        memory_kb = peak_memory / 1024

        print(f"  Part {partNo} Avg {avg_time:.5e} (in ms {avg_time * 1000}), "
              f"Min {min_time:.5e}, Max {max_time:.5e}, "
              f"Memory Used {memory_kb:.0f} KB.")

    total_elapsed = time.time() - total_start
    print(f"Benchmarking 2025 done in time: {total_elapsed:.5e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <day_number> [test] [part] [bench]")
        sys.exit(1)

    day = sys.argv[1]
    test = False
    part = None
    benchmark = False

    for i in range(2, len(sys.argv)):
        arg = sys.argv[i]
        if arg.lower() == "test":
            test = True
        elif arg.lower() == "bench":
            benchmark = True
        elif arg.isdigit():
            part = int(arg)

    run_solution(day, test, part, benchmark)