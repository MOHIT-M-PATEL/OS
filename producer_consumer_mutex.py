import threading
import queue
import random
import time

BUFFER_SIZE = 5
ITEMS_TO_PRODUCE = 10
PRODUCER_COUNT = 2
CONSUMER_COUNT = 2

buffer = queue.Queue(BUFFER_SIZE)  # Shared buffer


# Producer function
def producer(producer_id):
    for i in range(ITEMS_TO_PRODUCE):
        item = random.randint(1, 100)  # Produce a random number
        try:
            buffer.put(item, timeout=2)  # Add item to the buffer with timeout
            print(f"Producer {producer_id} inserting {item} in slot {buffer.qsize() - 1}")
        except queue.Full:
            print(f"Producer {producer_id} blocked....... buffer full!")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work


# Consumer function
def consumer(consumer_id):
    for _ in range(ITEMS_TO_PRODUCE):
        try:
            item = buffer.get(timeout=2)  # Remove item from the buffer with timeout
            print(f"Consumer {consumer_id} consuming {item} from slot {buffer.qsize()}")
            buffer.task_done()
        except queue.Empty:
            print(f"Consumer {consumer_id} blocked....... buffer empty!")
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
