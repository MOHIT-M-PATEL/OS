#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define MAX_STRING_LEN 10
#define PRODUCER_COUNT 2
#define CONSUMER_COUNT 2
#define ITEMS_TO_PRODUCE 10

char buffer[BUFFER_SIZE][MAX_STRING_LEN]; // Buffer to hold strings
int in = 0, out = 0, count = 0;
pthread_mutex_t mutex;
pthread_cond_t full, empty;

void* producer(void* arg) {
    int id = *(int*)arg;
    for (int i = 0; i < ITEMS_TO_PRODUCE; i++) {
        pthread_mutex_lock(&mutex);

        while (count == BUFFER_SIZE) {
            printf("Producer %d blocked....... buffer full!\n", id);
            pthread_cond_wait(&empty, &mutex);
        }

        int item = rand() % 100; // Produce a random number
        snprintf(buffer[in], MAX_STRING_LEN, "%d", item);
        printf("Producer %d inserting %d in slot %d\n", id, item, in);

        in = (in + 1) % BUFFER_SIZE;
        count++;

        pthread_cond_signal(&full);
        pthread_mutex_unlock(&mutex);

        sleep(rand() % 2); // Simulate work
    }
    return NULL;
}

void* consumer(void* arg) {
    int id = *(int*)arg;
    for (int i = 0; i < ITEMS_TO_PRODUCE; i++) {
        pthread_mutex_lock(&mutex);

        while (count == 0) {
            printf("Consumer %d blocked....... buffer empty!\n", id);
            pthread_cond_wait(&full, &mutex);
        }

        int item;
        sscanf(buffer[out], "%d", &item); // Consume the item
        printf("Consumer %d consuming %d from slot %d\n", id, item, out);

        out = (out + 1) % BUFFER_SIZE;
        count--;

        pthread_cond_signal(&empty);
        pthread_mutex_unlock(&mutex);

        sleep(rand() % 2); // Simulate work
    }
    return NULL;
}

int main() {
    pthread_t producers[PRODUCER_COUNT], consumers[CONSUMER_COUNT];
    int producer_ids[PRODUCER_COUNT], consumer_ids[CONSUMER_COUNT];

    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&full, NULL);
    pthread_cond_init(&empty, NULL);

    // Create producer threads
    for (int i = 0; i < PRODUCER_COUNT; i++) {
        producer_ids[i] = i + 1;
        pthread_create(&producers[i], NULL, producer, &producer_ids[i]);
    }

    // Create consumer threads
    for (int i = 0; i < CONSUMER_COUNT; i++) {
        consumer_ids[i] = i + 1;
        pthread_create(&consumers[i], NULL, consumer, &consumer_ids[i]);
    }

    // Join producer threads
    for (int i = 0; i < PRODUCER_COUNT; i++) {
        pthread_join(producers[i], NULL);
    }

    // Join consumer threads
    for (int i = 0; i < CONSUMER_COUNT; i++) {
        pthread_join(consumers[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&full);
    pthread_cond_destroy(&empty);

    return 0;
}
