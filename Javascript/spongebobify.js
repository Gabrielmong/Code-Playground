function spongebobify(str) {
  return str
    .split("")
    .map((char, index) => {
      return index % 2 === 0 ? char.toUpperCase() : char.toLowerCase();
    })
    .join("");
}

console.log(spongebobify("spongebob"));
