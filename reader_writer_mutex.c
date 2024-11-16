#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

// Shared data (hours, minutes, seconds)
int hours = 23, minutes = 59, seconds = 55;

// Mutex to control access to the shared resource
pthread_mutex_t timer_lock;

// Writer function
void* writer(void* arg) {
    int writer_id = *(int*)arg; // Get writer ID
    while (1) {
        // Lock the mutex to enter the critical section
        pthread_mutex_lock(&timer_lock);

        // Critical section (writing)
        printf("writer %d writing clock %02d:%02d:%02d\n", writer_id, hours, minutes, seconds);
        seconds = (seconds + 1) % 60;
        if (seconds == 0) {
            minutes = (minutes + 1) % 60;
            if (minutes == 0) {
                hours = (hours + 1) % 24;
            }
        }

        // Unlock the mutex
        pthread_mutex_unlock(&timer_lock);

        // Sleep for a while
        sleep(2);
    }
    return NULL;
}

// Reader function
void* reader(void* arg) {
    int reader_id = *(int*)arg; // Get reader ID
    while (1) {
        // Lock the mutex to enter the critical section
        pthread_mutex_lock(&timer_lock);

        // Critical section (reading)
        printf("reader %d reading clock %02d:%02d:%02d\n", reader_id, hours, minutes, seconds);

        // Unlock the mutex
        pthread_mutex_unlock(&timer_lock);

        // Indicate exiting the critical section
        printf("reader %d exiting critical section\n", reader_id);

        // Sleep for a while
        sleep(1);
    }
    return NULL;
}

int main() {
    // Thread identifiers
    pthread_t writerThreads[2], readerThreads[3];
    int writer_ids[2] = {1, 2};
    int reader_ids[3] = {1, 2, 3};

    // Initialize the mutex
    pthread_mutex_init(&timer_lock, NULL);

    // Create writer threads
    for (int i = 0; i < 2; i++) {
        pthread_create(&writerThreads[i], NULL, writer, &writer_ids[i]);
    }

    // Create reader threads
    for (int i = 0; i < 3; i++) {
        pthread_create(&readerThreads[i], NULL, reader, &reader_ids[i]);
    }

    // Join threads (infinite loop, so these will not terminate)
    for (int i = 0; i < 2; i++) {
        pthread_join(writerThreads[i], NULL);
    }
    for (int i = 0; i < 3; i++) {
        pthread_join(readerThreads[i], NULL);
    }

    // Destroy the mutex
    pthread_mutex_destroy(&timer_lock);

    return 0;
}
