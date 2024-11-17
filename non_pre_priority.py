import random

# Function to implement Non-Preemptive Priority scheduling
def non_preemptive_priority(processes, n, at, bt, priority):
    wt = [0] * n  # Waiting time for each process
    tat = [0] * n  # Turnaround time for each process
    ft = [0] * n  # Finish time for each process
    remaining_bt = bt[:]  # Create a copy of burst times for internal processing
    time_elapsed = 0  # Current time

    remaining_processes = n  # Track the number of remaining processes

    while remaining_processes > 0:
        # Collect available processes based on arrival time
        available_processes = [i for i in range(n) if at[i] <= time_elapsed and remaining_bt[i] > 0]
        
        if available_processes:
            # Select the process with the highest priority (lowest numerical value)
            current_process = min(available_processes, key=lambda x: (priority[x], at[x]))
            
            # Update time elapsed and finish time for the current process
            time_elapsed += remaining_bt[current_process]
            ft[current_process] = time_elapsed
            
            # Calculate turnaround time and waiting time
            tat[current_process] = ft[current_process] - at[current_process]
            wt[current_process] = tat[current_process] - bt[current_process]
            
            # Mark the current process as finished
            remaining_bt[current_process] = 0  # Set remaining burst time to zero
            remaining_processes -= 1  # Decrement the count of remaining processes
        else:
            # No process is available, jump to the next arrival time
            next_arrival = min(at[i] for i in range(n) if remaining_bt[i] > 0)
            time_elapsed = next_arrival  # Move the time forward to the next arrival time

    return wt, tat, ft


# Function to display the results table
def display_results(processes, n, at, bt, ft, tat, wt):
    print(f"{'Processes':<10} {'AT':<10} {'BT':<10} {'FT':<10} {'TT':<10} {'WT':<10}")
    
    for i in range(n):
        print(f"{processes[i]:<10} {at[i]:<10} {bt[i]:<10} {ft[i]:<10} {tat[i]:<10} {wt[i]:<10}")

# Main function to execute Non-Preemptive Priority scheduling
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3, 4]
    n = len(processes)
    
    # Generate random arrival and burst times for each process
    arrival_time = [random.randint(0, 5) for _ in range(n)]
    burst_time = [random.randint(1, 10) for _ in range(n)]
    # Generate random priorities for each process (lower number = higher priority)
    priority = [random.randint(1, 5) for _ in range(n)]
    # priority = [4,3,2,1]

    # Print generated values for debugging
    print(f"Arrival Times: {arrival_time}")
    print(f"Burst Times: {burst_time}")
    print(f"Priorities: {priority}")

    # Calculate waiting time, finish time, and turnaround time using Non-Preemptive Priority
    waiting_time, turnaround_time, finish_time = non_preemptive_priority(processes, n, arrival_time, burst_time, priority)
    
    # Display the results
    display_results(processes, n, arrival_time, burst_time, finish_time, turnaround_time, waiting_time)
