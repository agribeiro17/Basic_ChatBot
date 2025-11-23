// web_chatbot/static/script.js
const chatBox = document.getElementById('chat-box');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const userMessage = userInput.value;
    if (!userMessage) {
        return;
    }

    appendMessage(userMessage, 'user-message');
    userInput.value = '';

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            appendMessage(`Error: ${data.error}`, 'bot-message');
        } else {
            appendMessage(data.response, 'bot-message');
        }
    })
    .catch(error => {
        appendMessage(`Error: ${error}`, 'bot-message');
    });
});

function appendMessage(message, className) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', className);
    const p = document.createElement('p');
    p.textContent = message;
    messageElement.appendChild(p);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
