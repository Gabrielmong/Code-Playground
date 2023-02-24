#!/bin/sh

start=$(date +%s.%N)
echo "Started in a bash script"
i=0
primes=0
while [ $i -lt 100000 ]
do
  isPrime=true
  j=2
  while [ $j -lt $i ]
  do
    if [ $(($i % $j)) -eq 0 ]
    then
      isPrime=false
      break
    fi
    echo "primes found: $primes"
    j=$(($j + 1))
  done
  if $isPrime
  then
    primes=$(($primes + 1))
  fi
  i=$(($i + 1))
done
end=$(date +%s.%N)
time=$(echo "$end - $start" | bc)
echo "Execution time: $time seconds"
echo "Primes found: $primes"
echo "Primes per second: $(echo "$primes / $time" | bc)"
