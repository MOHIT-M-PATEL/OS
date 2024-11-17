def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)  # Remove the first page (FIFO)
                memory.append(page)
            page_faults += 1
        # Print memory state for each step (Optional)
        print("Memory:", memory)
    return page_faults


def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    page_index = {}

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Find the least recently used page by using `page_index`
                lru_page = min(memory, key=lambda p: page_index[p])
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        # Update the index of the current page to the latest access
        page_index[page] = i
        # Print memory state for each step (Optional)
        print("Memory:", memory)
    return page_faults



def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Find the page that will not be used for the longest time
                future_indices = []
                for mem_page in memory:
                    if mem_page in pages[i+1:]:
                        future_indices.append(pages[i+1:].index(mem_page))
                    else:
                        future_indices.append(float('inf'))
                # Replace the page that won't be used for the longest time
                replace_index = future_indices.index(max(future_indices))
                memory[replace_index] = page
            page_faults += 1
        # Print memory state for each step (Optional)
        print("Memory:", memory)
    return page_faults


# Test cases
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3

print("FIFO Page Faults:", fifo_page_replacement(pages, capacity))
print("LRU Page Faults:", lru_page_replacement(pages, capacity))
print("Optimal Page Faults:", optimal_page_replacement(pages, capacity))
