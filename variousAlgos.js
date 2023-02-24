function quickSort(arr, left, right) {
  var len = arr.length,
    pivot,
    partitionIndex;

  if (left < right) {
    pivot = right;
    partitionIndex = partition(arr, pivot, left, right);

    quickSort(arr, left, partitionIndex - 1);
    quickSort(arr, partitionIndex + 1, right);
  }
  return arr;
}

function partition(arr, pivot, left, right) {
  var pivotValue = arr[pivot],
    partitionIndex = left;

  for (var i = left; i < right; i++) {
    if (arr[i] < pivotValue) {
      swap(arr, i, partitionIndex);
      partitionIndex++;
    }
  }
  swap(arr, right, partitionIndex);
  return partitionIndex;
}

function swap(arr, i, j) {
  var temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}
console.log(
  "Quick Sort \n",
  "[100,-3,2,4,6,9,1,2,5,3,23], 0, 10 \n",
  quickSort([100, -3, 2, 4, 6, 9, 1, 2, 5, 3, 23], 0, 10),
  "\n"
);

function bubbleSort(arr) {
  var noSwaps;
  for (var i = arr.length; i > 0; i--) {
    noSwaps = true;
    for (var j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        var temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        noSwaps = false;
      }
    }
    if (noSwaps) break;
  }
  return arr;
}

console.log(
  "Bubble \n",
  "[8,1,2,3,4,5,6,7] \n",
  bubbleSort([8, 1, 2, 3, 4, 5, 6, 7]),
  "\n"
);

function selectionSort(arr) {
  for (var i = 0; i < arr.length; i++) {
    var lowest = i;
    for (var j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[lowest]) {
        lowest = j;
      }
    }
    if (i !== lowest) {
      //SWAP!
      var temp = arr[i];
      arr[i] = arr[lowest];
      arr[lowest] = temp;
    }
  }
  return arr;
}

console.log(
  "Selection \n",
  "[0,2,34,22,10,19,17] \n",
  selectionSort([0, 2, 34, 22, 10, 19, 17]),
  "\n"
);

function insertionSort(arr) {
  for (var i = 1; i < arr.length; i++) {
    var currentVal = arr[i];
    for (var j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
      arr[j + 1] = arr[j];
    }
    arr[j + 1] = currentVal;
  }
  return arr;
}

console.log(
  "Insertion \n",
  "[2,1,9,76,4] \n",
  insertionSort([2, 1, 9, 76, 4]),
  "\n"
);

function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  var mid = Math.floor(arr.length / 2);
  var left = mergeSort(arr.slice(0, mid));
  var right = mergeSort(arr.slice(mid));
  return merge(left, right);
}

function merge(left, right) {
  var result = [];
  var leftIndex = 0;
  var rightIndex = 0;
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }
  return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}

console.log("Merge \n", "[10,24,76,73] \n", mergeSort([10, 24, 76, 73]), "\n");

function radixSort(arr) {
  var maxDigitCount = mostDigits(arr);

  for (var k = 0; k < maxDigitCount; k++) {
    var digitBuckets = Array.from({ length: 10 }, () => []);
    for (var i = 0; i < arr.length; i++) {
      var digit = getDigitFrom(arr[i], k);
      digitBuckets[digit].push(arr[i]);
    }
    arr = [].concat(...digitBuckets);
  }
  return arr;
}

function getDigitFrom(num, i) {
  return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
}

function digitCount(num) {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}

function mostDigits(nums) {
  var maxDigits = 0;
  for (var i = 0; i < nums.length; i++) {
    maxDigits = Math.max(maxDigits, digitCount(nums[i]));
  }
  return maxDigits;
}

console.log(
  "Radix \n",
  "[23,345,5467,12,2345,9852] \n",
  radixSort([23, 345, 5467, 12, 2345, 9852]),
  "\n"
);

function binarySearch(arr, target) {
  let start = 0;
  let end = arr.length - 1;
  let middle = Math.floor((start + end) / 2);

  while (arr[middle] !== target && start <= end) {
    if (target < arr[middle]) {
      end = middle - 1;
    } else {
      start = middle + 1;
    }

    middle = Math.floor((start + end) / 2);
  }
  return arr[middle] === target ? middle : -1;
}

console.log(
  "Binary\n ",
  "[2, 5, 6, 9, 13, 15, 28, 30] \n",
  binarySearch([2, 5, 6, 9, 13, 15, 28, 30], 103),
  "\n"
);

function binarySearchRecursive(arr, target, start, end) {
  if (start > end) return -1;
  let middle = Math.floor((start + end) / 2);
  if (arr[middle] === target) return middle;
  if (arr[middle] > target)
    return binarySearchRecursive(arr, target, start, middle - 1);
  return binarySearchRecursive(arr, target, middle + 1, end);
}

console.log(
  "Binary recursive \n",
  "[2, 5, 6, 9, 13, 15, 28, 30], 15, 9, 7 \n",
  binarySearchRecursive([2, 5, 6, 9, 13, 15, 28, 30], 15, 0, 7),
  "\n"
);

function naiveSearch(long, short) {
  let count = 0;
  for (let i = 0; i < long.length; i++) {
    for (let j = 0; j < short.length; j++) {
      if (short[j] !== long[i + j]) break;
      if (j === short.length - 1) count++;
    }
  }
  return count;
}

console.log(
  "Naive \n",
  "lorie loled, lol\n",
  naiveSearch("lorie loled", "lol"),
  "\n"
);

function sameFrequency(num1, num2) {
  let strNum1 = num1.toString();
  let strNum2 = num2.toString();
  if (strNum1.length !== strNum2.length) return false;

  let lookup = {};

  for (let i = 0; i < strNum1.length; i++) {
    let digit = strNum1[i];
    lookup[digit] ? (lookup[digit] += 1) : (lookup[digit] = 1);
  }

  for (let i = 0; i < strNum2.length; i++) {
    let digit = strNum2[i];
    if (!lookup[digit]) return false;
    else lookup[digit] -= 1;
  }

  return true;
}

console.log("Same frequency \n", "182, 281 \n", sameFrequency(182, 281), "\n");

function areThereDuplicates() {
  let collection = {};

  for (let val in arguments) {
    collection[arguments[val]] = (collection[arguments[val]] || 0) + 1;
  }

  for (let key in collection) {
    if (collection[key] > 1) return true;
  }

  return false;
}

console.log(
  "Are there duplicates \n",
  "1, 2, 3 \n",
  areThereDuplicates(1, 2, 3),
  "\n"
);

function averagePair(arr, num) {
  let start = 0;
  let end = arr.length - 1;
  while (start < end) {
    let avg = (arr[start] + arr[end]) / 2;
    if (avg === num) return true;
    else if (avg < num) start++;
    else end--;
  }
  return false;
}

console.log(
  "Average pair \n",
  "[1, 2, 3], 2.5 \n",
  averagePair([1, 2, 3], 2.5),
  "\n"
);

function isSubsequence(str1, str2) {
  let i = 0;
  let j = 0;
  if (!str1) return true;
  while (j < str2.length) {
    if (str2[j] === str1[i]) i++;
    if (i === str1.length) return true;
    j++;
  }
  return false;
}

console.log(
  "Is subsequence \n",
  "hello, hello world\n",
  isSubsequence("hello", "hello world"),
  "\n"
);

function maxSubarraySum(arr, num) {
  let maxSum = 0;
  let tempSum = 0;
  if (arr.length < num) return null;
  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }
  tempSum = maxSum;
  for (let i = num; i < arr.length; i++) {
    tempSum = tempSum - arr[i - num] + arr[i];
    maxSum = Math.max(maxSum, tempSum);
  }
  return maxSum;
}

console.log(
  "Max subarray sum \n",
  "[2,3,1,2,4,3], 2 \n",
  maxSubarraySum([2, 3, 1, 2, 4, 3], 2),
  "\n"
);

function minSubArrayLen(arr, num) {
  let total = 0;
  let start = 0;
  let end = 0;
  let minLen = Infinity;

  while (start < arr.length) {
    if (total < num && end < arr.length) {
      total += arr[end];
      end++;
    } else if (total >= num) {
      minLen = Math.min(minLen, end - start);
      total -= arr[start];
      start++;
    } else {
      break;
    }
  }

  return minLen === Infinity ? 0 : minLen;
}

console.log(
  "Min subarray length \n",
  "[2,3,1,2,4,3], 7 \n",
  minSubArrayLen([2, 3, 1, 2, 4, 3], 7),
  "\n"
);

function findLongestSubstring(str) {
  let longest = 0;
  let seen = {};
  let start = 0;

  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (seen[char]) {
      start = Math.max(start, seen[char]);
    }
    // index - beginning of substring + 1 (to include current in count)
    longest = Math.max(longest, i - start + 1);
    // store the index of the next char so as to not double count
    seen[char] = i + 1;
  }
  return longest;
}

console.log(
  "Longest substring \n",
  "rithmschool \n",
  findLongestSubstring("rithmschool"),
  "\n"
);

function countUniqueValues(arr) {
  if (arr.length === 0) return 0;
  let i = 0;
  for (let j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j];
    }
  }
  return i + 1;
}

console.log(
  "Count unique values \n",
  "[1,1,1,1,1,2] \n",
  countUniqueValues([1, 1, 1, 1, 1, 2]),
  "\n"
);
