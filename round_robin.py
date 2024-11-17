import random

# Function to implement Round Robin scheduling
def round_robin(processes, n, at, bt, quantum):
    remaining_bt = bt[:]  # Copy of burst times for remaining burst time tracking
    wt = [0] * n  # Waiting time for each process
    tat = [0] * n  # Turnaround time for each process
    ft = [0] * n  # Finish time for each process
    time_elapsed = 0  # Current time

    remaining_processes = n

    # While there are processes left to schedule
    while remaining_processes > 0:
        done = True
        for i in range(n):
            # Check if process has remaining burst time and has arrived
            if remaining_bt[i] > 0:
                done = False  # There are still processes left
                
                # Ensure we wait until process arrival time
                if time_elapsed < at[i]:
                    time_elapsed = at[i]
                
                start_time = time_elapsed

                # If remaining burst time is greater than quantum
                if remaining_bt[i] > quantum:
                    time_elapsed += quantum
                    remaining_bt[i] -= quantum
                else:
                    # If remaining burst time is less than or equal to quantum
                    time_elapsed += remaining_bt[i]
                    remaining_bt[i] = 0
                    ft[i] = time_elapsed
                    tat[i] = ft[i] - at[i]
                    wt[i] = tat[i] - bt[i]
                    remaining_processes -= 1

                end_time = time_elapsed

        if done:  # All processes are finished
            break

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
    
    # Calculate and display average waiting and turnaround time
    # print(f"\nAverage waiting time = {total_wt / n:.2f}")
    # print(f"Average turnaround time = {total_tat / n:.2f}")

# Main function to execute Round Robin scheduling
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3, 4]
    n = len(processes)
    
    # Generate random arrival and burst times for each process
    arrival_time = [random.randint(0, 5) for _ in range(n)]
    burst_time = [random.randint(1, 10) for _ in range(n)]
    quantum = 3  # Define the time quantum
    
    # Calculate waiting time, finish time, and turnaround time using Round Robin
    waiting_time, turnaround_time, finish_time = round_robin(processes, n, arrival_time, burst_time, quantum)
    
    # Display the results
    display_results(processes, n, arrival_time, burst_time, finish_time, turnaround_time, waiting_time)
