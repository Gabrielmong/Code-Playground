let start = new Date().getTime()
console.log('Started in JavaScript')
let i = 0
let primes = 0
while (i < 150000) {
  let isPrime = true
  for (let j = 2; j < i; j++) {
    if (i % j === 0) {
      isPrime = false
      break
    }
  }
  if (isPrime) {
    primes++
  }
  i++
}
let end = new Date().getTime()
let time = end - start
console.log('Execution time: ' + time / 1000 + ' seconds')
console.log('Primes found: ' + primes)
console.log('Primes per second: ' + (primes / time * 1000))

