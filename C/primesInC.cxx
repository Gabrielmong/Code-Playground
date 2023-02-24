#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int main() {
    clock_t start = clock();
    printf("Started in C\n");
    int i = 0;
    int primes = 0;
    while (i < 150000) {
        bool isPrime = true;
        for (int j = 2; j < i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes++;
        }
        i++;
    }
    clock_t end = clock();
    double time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Execution time: %f seconds\n", time);
    printf("Primes found: %d\n", primes);
    printf("Primes per second: %f\n", primes / time);

    getchar();
    return 0;
}