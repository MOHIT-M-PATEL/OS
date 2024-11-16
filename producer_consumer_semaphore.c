#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define MAX_STRING_LEN 10 // Maximum length for the produced string

char buffer[BUFFER_SIZE][MAX_STRING_LEN]; // Buffer to hold strings
int in = 0, out = 0;
sem_t bfull, bempty; // Semaphore for full and empty slots

// Function to produce a string
void* producer(void* arg) {
    char item[MAX_STRING_LEN];
    for (int i = 0; i < 10; i++) { // Produce 10 strings
        sem_wait(&bempty); // Wait for empty slot
        snprintf(item, MAX_STRING_LEN, "Item%d", i); // Produce an item within the max length
        strncpy(buffer[in], item, MAX_STRING_LEN); // Add string to buffer
        printf("Produced: %s\n", item);
        in = (in + 1) % BUFFER_SIZE; // Circular increment
        sem_post(&bfull); // Signal that there is a new item
        sleep(rand() % 2); // Sleep for a random time
    }
    return NULL;
}

// Function to consume a string
void* consumer(void* arg) {
    for (int i = 0; i < 10; i++) { // Consume 10 strings
        sem_wait(&bfull); // Wait for a full slot
        char item[MAX_STRING_LEN];
        strncpy(item, buffer[out], MAX_STRING_LEN); // Get string from buffer
        printf("Consumed: %s\n", item);
        out = (out + 1) % BUFFER_SIZE; // Circular increment
        sem_post(&bempty); // Signal that there is an empty slot
        sleep(rand() % 2); // Sleep for a random time
    }
    return NULL;
}

int main() {
    pthread_t prod, cons;
    sem_init(&bfull, 0, 0); // Initialize semaphore bfull to 0
    sem_init(&bempty, 0, BUFFER_SIZE); // Initialize semaphore bempty to BUFFER_SIZE

    // Create producer and consumer threads
    pthread_create(&prod, NULL, producer, NULL);
    pthread_create(&cons, NULL, consumer, NULL);

    // Join threads
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);

    sem_destroy(&bfull); // Destroy semaphore
    sem_destroy(&bempty); // Destroy semaphore
    return 0;
}
