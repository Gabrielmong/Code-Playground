public class primes {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        System.out.println("Started in Java");
        int i = 0;
        int primes = 0;
        while (i < 150000) {
            boolean isPrime = true;
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
        long end = System.currentTimeMillis();
        double time = (end - start) / 1000.0;
        System.out.println("Execution time: " + time + " seconds");
        System.out.println("Primes found: " + primes);
        System.out.println("Primes per second: " + (primes / time));
    }
}