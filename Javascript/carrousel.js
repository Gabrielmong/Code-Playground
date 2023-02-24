var message = "Que verga";

const carrousel = (message, firstCheck) => {

  if (firstCheck) {
    if (message[message.length - 1] !== " ") {
        message += " - ";
    }
  }

  if (message.length > 0) {
    console.clear();
    console.log(message.slice(0, 15));
    setTimeout(() => {
      carrousel(message.slice(1) + message[0], false);
    }, 250);
  }
}

carrousel(message, true);
