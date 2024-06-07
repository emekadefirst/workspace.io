var ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function (event) {
  var messages = document.getElementById("messages");
  var message = document.createElement("li");
  var content = document.createTextNode(event.data);
  message.appendChild(content);
  messages.appendChild(message);
};

function sendMessage(event) {
  var input = document.getElementById("messageText");
  ws.send(input.value);
  input.value = "";
  event.preventDefault();
}

function fetchMessages() {
  fetch("http://localhost:8000/message")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const messages = data.messages; // Assuming data is an array of messages

      const messageList = document.getElementById("message-list");
      messageList.innerHTML = ""; // Clear existing messages

      messages.forEach((message) => {
        const li = document.createElement("li");
        li.textContent = message.text; // Assuming each message has a 'text' field
        messageList.appendChild(li);
      });
    })
    .catch((error) => {
      console.error("Error fetching messages:", error);
    });
}
fetchMessages()
