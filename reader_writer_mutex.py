import threading
import time

# Shared data (hours, minutes, seconds)
hours, minutes, seconds = 23, 59, 55

# Mutex to control access to the shared resource
timer_lock = threading.Lock()

# Counter to limit output
entry_count = 0
max_entries = 25

# Condition to stop threads
stop_threads = threading.Event()


# Writer function
def writer(writer_id):
    global hours, minutes, seconds, entry_count
    while not stop_threads.is_set():
        with timer_lock:  # Automatically acquires and releases the lock
            if entry_count >= max_entries:
                stop_threads.set()
                return
            print(f"writer {writer_id} writing clock {hours:02}:{minutes:02}:{seconds:02}\n")
            entry_count += 1
            seconds = (seconds + 1) % 60
            if seconds == 0:
                minutes = (minutes + 1) % 60
                if minutes == 0:
                    hours = (hours + 1) % 24
        time.sleep(2)  # Simulate periodic writing


# Reader function
def reader(reader_id):
    global entry_count
    while not stop_threads.is_set():
        with timer_lock:  # Automatically acquires and releases the lock
            if entry_count >= max_entries:
                stop_threads.set()
                return
            print(f"reader {reader_id} reading clock {hours:02}:{minutes:02}:{seconds:02}\n")
            entry_count += 1
        print(f"reader {reader_id} exiting critical section\n")
        time.sleep(1)  # Simulate periodic reading


# Main function to create threads
def main():
    # Create writer threads
    writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(1, 3)]

    # Create reader threads
    reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(1, 4)]

    # Start all threads
    for thread in writer_threads + reader_threads:
        thread.start()

    # Join all threads
    for thread in writer_threads + reader_threads:
        thread.join()


if __name__ == "__main__":
    main()
