function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function demo() {
  for (let i = 0; i < 23; i++) {
    for (let j = 0; j < 59; j++) {
      for (let l = 0; l < 59; l++) {
        console.clear();
        console.log(i + ":" + j + ":" + l);
        await sleep(1000);
      }
    }
  }

    demo();
}

demo();
