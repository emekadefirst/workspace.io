// Function to scroll to the bottom of the messages
function scrollToBottom() {
  const chatMessagesElement = document.getElementById("chat-messages");
  chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
}

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
    // Scroll to the bottom after loading messages
    scrollToBottom();
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });

var ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = function (event) {
  const messagesElement = document.getElementById("messages");
  const message = document.createElement("li");
  const content = document.createTextNode(event.data);
  message.appendChild(content);
  messagesElement.appendChild(message);
  // Scroll to the bottom when a new message arrives
  scrollToBottom();
};

function sendMessage(event) {
  const input = document.getElementById("messageText");
  ws.send(input.value);
  input.value = "";
  event.preventDefault();
}
