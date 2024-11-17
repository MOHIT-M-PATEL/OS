import random

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time  # Initialize remaining time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def preemptive_sjf(processes):
    time = 0
    remaining_processes = processes[:]  # Create a copy of the original processes
    current_process = None
    last_switch_time = 0  # Track the last time a process switch occurred

    while remaining_processes:
        # Get available processes based on arrival time
        available_processes = [p for p in remaining_processes if p.arrival_time <= time]

        if not available_processes:
            # No process is available, increment time
            time += 1
            if current_process:
                current_process = None  # Reset current process
            continue

        # Find the process with the shortest remaining time
        shortest_job = min(available_processes, key=lambda p: p.remaining_time)

        if current_process != shortest_job:
            current_process = shortest_job
            last_switch_time = time

        # Execute the current process
        current_process.remaining_time -= 1
        time += 1

        # If the current process has finished execution
        if current_process.remaining_time == 0:
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            remaining_processes.remove(current_process)
            current_process = None

    return remaining_processes

def display_results(processes):
    print(f"{'PID':<5} {'AT':<10} {'BT':<10} {'FT':<10} {'TT':<10} {'WT':<10}")
    for p in processes:
        print(f"{p.pid:<5} {p.arrival_time:<10} {p.burst_time:<10} {p.completion_time:<10} {p.turnaround_time:<10} {p.waiting_time:<10}")

# Example usage
if __name__ == "__main__":
    # Generate random arrival and burst times for processes
    num_processes = 4
    processes = []
    for i in range(num_processes):
        arrival_time = random.randint(0, 5)  # Random arrival time between 0 and 5
        burst_time = random.randint(1, 10)    # Random burst time between 1 and 10
        processes.append(Process(i + 1, arrival_time, burst_time))

    # Print generated values for debugging
    # print("Processes:")
    # for p in processes:
    #     print(f"PID: {p.pid}, Arrival Time: {p.arrival_time}, Burst Time: {p.burst_time}")

    # Run Preemptive SJF scheduling
    preemptive_sjf(processes)

    # Display results in a formatted table
    display_results(processes)
