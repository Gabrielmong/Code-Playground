// calculate pi

var pi = 0;
var n = 100000000000000000000;
var sign = 1;
for (var i = 1; i < n; i += 2) {
    pi += sign * 4 / i;
    sign = -sign;
}
console.log(pi);
