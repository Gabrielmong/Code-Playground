#include <iostream>
#include <chrono>

using namespace std;

int main()
{
    auto start = chrono::high_resolution_clock::now();
    cout << "Started in C++" << endl;
    int i = 0;
    int primes = 0;
    while (i < 150000)
    {
        bool isPrime = true;
        for (int j = 2; j < i; j++)
        {
            if (i % j == 0)
            {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
        {
            primes++;
        }
        i++;
    }
    auto end = chrono::high_resolution_clock::now();
    auto time = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << "Execution time: " << time / 1000.0 << " seconds" << endl;
    cout << "Primes found: " << primes << endl;
    cout << "Primes per second: " << (primes / (time / 1000.0)) << endl;

    cin.get();
    return 0;
}