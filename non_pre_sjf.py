import random

# Function to implement Non-Preemptive Shortest Job First scheduling
def non_preemptive_sjf(processes, n, at, bt):
    remaining_bt = bt[:]  # Copy of burst times for remaining burst time tracking
    wt = [0] * n  # Waiting time for each process
    tat = [0] * n  # Turnaround time for each process
    ft = [0] * n  # Finish time for each process
    time_elapsed = 0  # Current time

    # Create a list of processes with their arrival times and burst times
    process_list = sorted(zip(processes, at, bt), key=lambda x: (x[1], x[2]))

    while process_list:
        # Filter processes that have arrived by the current time
        available_processes = [p for p in process_list if p[1] <= time_elapsed]

        if not available_processes:  # If no processes are available, jump to next arrival
            time_elapsed = process_list[0][1]
            continue

        # Select the process with the shortest burst time
        next_process = min(available_processes, key=lambda x: x[2])

        process_id, arrival_time, burst_time = next_process
        process_list.remove(next_process)  # Remove selected process from the list
        
        time_elapsed += burst_time  # Increment time by the burst time of selected process
        ft[process_id - 1] = time_elapsed  # Finish time is current time
        tat[process_id - 1] = ft[process_id - 1] - arrival_time  # Turnaround time
        wt[process_id - 1] = tat[process_id - 1] - burst_time  # Waiting time

    return wt, tat, ft

# Function to display the results table
def display_results(processes, n, at, bt, ft, tat, wt):
    print(f"{'Processes':<10} {'AT':<10} {'BT':<10} {'FT':<10} {'TT':<10} {'WT':<10}")
    
    total_wt = 0  # Total waiting time
    total_tat = 0  # Total turnaround time
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{processes[i]:<10} {at[i]:<10} {bt[i]:<10} {ft[i]:<10} {tat[i]:<10} {wt[i]:<10}")
    

# Main function to execute Non-Preemptive SJF scheduling
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3, 4]
    n = len(processes)
    
    # Generate random arrival and burst times for each process
    arrival_time = [random.randint(0, 5) for _ in range(n)]
    burst_time = [random.randint(1, 10) for _ in range(n)]
    
    # Calculate waiting time, finish time, and turnaround time using Non-Preemptive SJF
    waiting_time, turnaround_time, finish_time = non_preemptive_sjf(processes, n, arrival_time, burst_time)
    
    # Display the results
    display_results(processes, n, arrival_time, burst_time, finish_time, turnaround_time, waiting_time)
