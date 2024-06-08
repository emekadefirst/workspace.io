// Fetch data from the endpoint
fetch("http://localhost:8000/message")
  .then((response) => response.json())
  .then((data) => {
    const messagesElement = document.getElementById("messages");
    // Clear existing content
    messagesElement.innerHTML = "";
    // Append each message to the list
    data.forEach((messageObj) => {
      const li = document.createElement("li");
      li.textContent = messageObj.message; // Use the 'message' property
      messagesElement.appendChild(li);
    });
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });
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
  input.value = '';
  event.preventDefault();
}
