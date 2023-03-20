const express = require("express");
const app = express();
const { v4: uuidv4 } = require("uuid");
const mongoose = require("mongoose");
const ws = require("ws");

const { Schema } = mongoose;
const { ObjectId } = Schema.Types;

const chatSchema = new Schema({
  _id: { type: ObjectId, auto: true },
  name: { type: String, required: false },
  message: { type: String, required: true },
  date: { type: Date, default: Date.now },
});

const server = app.listen(3000, () => {
  console.clear();
  console.log("Express server started on port 3000");
});

const Chat = mongoose.model("Chat", chatSchema);

mongoose.connect("mongodb://localhost:27017/chat", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;

db.on("error", (err) => {
  console.log(err);
});

db.once("open", () => {
  console.log("Connected to database");
});

const wss = new ws.Server({ server });

wss.on("connection", (ws) => {
  console.log("Client connected");

  ws.on("message", (message) => {
    const data = JSON.parse(message);
    const chat = new Chat(data);

    switch (data.type) {
      case "ADD_MESSAGE":
        try {
          chat.save();
        } catch (err) {
          console.log(err);
        }

        wss.clients.forEach((client) => {
          if (client.readyState === ws.OPEN && client !== ws) {
            client.send(JSON.stringify(data));
          }
        });

        break;
      case "GET_MESSAGES":
        try {
          Chat.find().then((messages) => {
            const data = {
              type: "GET_MESSAGES",
              messages,
            };
            ws.send(JSON.stringify(data));
          });
        } catch (err) {
          console.log(err);
        }
        break;
      default:
        break;
    }
  });

  ws.on("close", () => {
    console.log("Client disconnected");
  });
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static("public"), (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});
