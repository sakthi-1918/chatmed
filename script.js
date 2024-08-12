// script.js

function sendMessage() {
    const userInput = document.getElementById("user-input");
    const chatBody = document.getElementById("chat-body");

    // Get user input
    const userMessage = userInput.value.trim();
    if (userMessage === "") return;

    // Append user message to chat body
    const userMessageElement = document.createElement("div");
    userMessageElement.classList.add("message", "user");
    userMessageElement.innerHTML = `<p>${userMessage}</p>`;
    chatBody.appendChild(userMessageElement);

    // Clear input field
    userInput.value = "";

    // Simulate bot response
    const botResponse = getBotResponse(userMessage);
    const botMessageElement = document.createElement("div");
    botMessageElement.classList.add("message", "bot");
    botMessageElement.innerHTML = `<p>${botResponse}</p>`;
    chatBody.appendChild(botMessageElement);

    // Scroll to the bottom of the chat
    chatBody.scrollTop = chatBody.scrollHeight;
}

function getBotResponse(userMessage) {
    // Basic response logic (replace with actual AI backend)
    if (userMessage.toLowerCase().includes("anatomy")) {
        return "Anatomy refers to the structure of the human body.";
    } else if (userMessage.toLowerCase().includes("physiology")) {
        return "Physiology refers to the functions and processes of the human body.";
    } else {
        return "I'm not sure, but I can help you with anatomy or physiology-related questions!";
    }
}
