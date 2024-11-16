import threading
import random
import time

BUFFER_SIZE = 5
ITEMS_TO_PRODUCE = 10
PRODUCER_COUNT = 2
CONSUMER_COUNT = 2

# Shared buffer and synchronization primitives
buffer = [None] * BUFFER_SIZE
in_index = 0  # Points to the next insertion slot
out_index = 0  # Points to the next removal slot

# Semaphores
empty_slots = threading.Semaphore(BUFFER_SIZE)  # Tracks available slots
full_slots = threading.Semaphore(0)  # Tracks filled slots
buffer_lock = threading.Lock()  # Protects buffer access


# Producer function
def producer(producer_id):
    global in_index
    for _ in range(ITEMS_TO_PRODUCE):
        item = random.randint(1, 100)  # Produce a random number

        empty_slots.acquire()  # Wait for an empty slot
        with buffer_lock:  # Ensure exclusive access to the buffer
            buffer[in_index] = item
            print(f"Producer {producer_id} inserting {item} in slot {in_index}")
            in_index = (in_index + 1) % BUFFER_SIZE

        full_slots.release()  # Signal that a new item is available
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work


# Consumer function
def consumer(consumer_id):
    global out_index
    for _ in range(ITEMS_TO_PRODUCE):
        full_slots.acquire()  # Wait for a filled slot
        with buffer_lock:  # Ensure exclusive access to the buffer
            item = buffer[out_index]
            print(f"Consumer {consumer_id} consuming {item} from slot {out_index}")
            out_index = (out_index + 1) % BUFFER_SIZE

        empty_slots.release()  # Signal that a slot is now available
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work


# Main function
def main():
    producers = []
    consumers = []

    # Create producer threads
    for i in range(PRODUCER_COUNT):
        thread = threading.Thread(target=producer, args=(i + 1,))
        producers.append(thread)
        thread.start()

    # Create consumer threads
    for i in range(CONSUMER_COUNT):
        thread = threading.Thread(target=consumer, args=(i + 1,))
        consumers.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in producers:
        thread.join()

    for thread in consumers:
        thread.join()


if __name__ == "__main__":
    main()
