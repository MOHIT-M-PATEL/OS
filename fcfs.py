import random

# Function to calculate Waiting Time and Finish Time for all processes
def calculate_times(processes, n, at, bt, wt, ft, tat):
    # Calculate waiting time and finish time for each process
    time_elapsed = 0
    for i in range(n):
        # If process arrival time is later than the current time, wait until its arrival
        if time_elapsed < at[i]:
            time_elapsed = at[i]

        # Waiting time is the difference between current time and arrival time
        wt[i] = time_elapsed - at[i]
        
        # Finish time is the current time + burst time
        ft[i] = time_elapsed + bt[i]
        
        # Turnaround time is finish time minus arrival time
        tat[i] = ft[i] - at[i]
        
        # Update the current time for the next process
        time_elapsed += bt[i]

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

# Main function to execute FCFS scheduling
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3, 4]
    n = len(processes)
    
    # Generate random arrival and burst times for each process
    arrival_time = [random.randint(0, 5) for _ in range(n)]
    burst_time = [random.randint(1, 10) for _ in range(n)]
    
    # Initialize time arrays
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    # Calculate waiting time, finish time, and turnaround time
    calculate_times(processes, n, arrival_time, burst_time, waiting_time, finish_time, turnaround_time)
    
    # Display the results
    display_results(processes, n, arrival_time, burst_time, finish_time, turnaround_time, waiting_time)
