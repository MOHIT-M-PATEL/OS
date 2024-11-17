def bankers_algorithm(processes, available, max_need, allocation): 
 
    n_processes = len(processes) 
    n_resources = len(available) 
 
    # Calculate current need for each process 
    need = [[max_need[i][j] - allocation[i][j] 
             for j in range(n_resources)] 
            for i in range(n_processes)] 
 
    # Keep track of finished processes 
    finish = [False] * n_processes 
 
    # Keep track of safe sequence 
    safe_sequence = [] 
 
    # Make a copy of available resources 
    work = available.copy() 
 
    # Find a safe sequence 
    while len(safe_sequence) < n_processes: 
        found = False 
 
        # Try to find a process that can be completed 
        for p_idx in range(n_processes): 
            if not finish[p_idx]: 
                # Check if all resources are available 
                if all(need[p_idx][j] <= work[j] for j in range(n_resources)): 
                    # Add allocated resources back to available 
                    for j in range(n_resources): 
                        work[j] += allocation[p_idx][j] 
 
                    # Mark process as finished 
                    finish[p_idx] = True 
                    safe_sequence.append(processes[p_idx]) 
                    found = True 
                    break 
 
        # If no process could be found, system is unsafe 
        if not found: 
            return False, [] 

    return True, safe_sequence 
 
 
# Example usage 
if __name__ == "__main__": 
    # Example data 
    processes = ["P0", "P1", "P2", "P3", "P4"] 
    available = [3, 3, 2]  # Available instances of resources A, B, C 
 
    max_need = [ 
        [7, 5, 3],  # P0 
        [3, 2, 2],  # P1 
        [9, 0, 2],  # P2 
        [2, 2, 2],  # P3 
        [4, 3, 3]  # P4 
    ] 
 
    allocation = [ 
        [0, 1, 0],  # P0 
        [2, 0, 0],  # P1 
        [3, 0, 2],  # P2 
        [2, 1, 1],  # P3 
        [0, 0, 2]  # P4 
    ] 
 
    # Run the algorithm 
    is_safe, sequence = bankers_algorithm(processes, available, 
max_need, allocation) 
 
    # Print results 
    if is_safe: 
        print("System is in safe state!") 
        print("Safe sequence is:", " -> ".join(sequence)) 
    else: 
        print("System is NOT in safe state!") 
        print("Deadlock might occur!") 