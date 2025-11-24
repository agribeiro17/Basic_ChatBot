// --- SELECTING HTML ELEMENTS --- //
/*
- document.getElementById(...)`: This is a standard method in web browsers that searches the HTML document for an element with a
                                 specific id attribute
*/
const chatBox = document.getElementById('chat-box')
const chatForm = document.getElementById('chat-form')
const userInput = document.getElementById('user-input')

// --- EVENT LISTENER ---//
/*
 --- HANDLING FORM SUBMISSIONS ---
- chatForm.addEventListener('submit', ...): This attaches an "event listener" to the chat form. It tells the browser: "When the user
                                            tries to submit this form (either by clicking the submit button or pressing Enter in the
                                            input field), run the function I'm providing."

-`(e) => { ... }`: This is an "arrow function" that gets executed when the event happens. The e parameter is the "event object," which
                   contains information about the event that occurred.

- `e.preventDefault()`: This is a crucial step. By default, when a form is submitted, the browser will try to send the data to a server
                        and reload the page. preventDefault() stops this default browser behavior, allowing you to handle the
                        submission with your own JavaScript code without a page refresh.

*/
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // --- PROCESSING USER INPUT --- //
    const userMessage = userInput.value; // Gets the current text that the user has typed into the input field (userInput) and stores it in userMessage.
    if (!userMessage) {
        return;
    }

    appendMessage(userMessage, 'user-message'); // It passes the user's message and the CSS class 'user-message' to it. This is what makes the user's own message appear in the chatbox instantly.
    userInput.value = ''; // This clears the input field by setting its value to an empty string, so the user can start typing their next message.

    // --- SENDING THE MESSAGE TO THE SERVER --- //
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({message: userMessage}), // JSON.stringify() converts a JavaScript  object { message: userMessage } into a JSON string like '{"message": "Hello there!"}'. This is the format the FastAPI backend expects.
    })
    .then(response=>response.json())
    // Handling Server Response
    .then(data => {
        if (data.error) {
            appendMessage(`Error: ${data.error}`, 'bot-message')
        } else {
            appendMessage(data.response, 'bot-message')
        }
    })
    // Handling Error
    .catch(error => {
        appendMessage(`Error: ${error}`, 'bot-message')
    });
});

// --- APPEND FUNCTION --- //
/*
This is the helper function that adds any new message to the chat window.

   * function appendMessage(message, className) -> Defines a function that accepts two arguments: the text of the message and a CSS class
                                                   name.

   * messageElement.classList.add('message', className); -> Adds two CSS classes to the new <div>. It will always have the class message,
                                                            and it will also have the class passed in the className argument
                                                            ('user-message' or 'bot-message').

   * chatBox.appendChild(messageElement); -> Appends the newly created messageElement (the <div>) as the last child of the chatBox
                                             element, making it visible on the page.

   * chatBox.scrollTop = chatBox.scrollHeight; -> This is a nice user-experience touch. It automatically scrolls the chatbox to the bottom
                                                  so that the newest message is always visible. scrollHeight is the total height of
                                                  the content inside the chatbox, and scrollTop is the amount it's scrolled down.
                                                  Setting them equal scrolls it all the way down.
*/

function appendMessage(message, className) {
    const messageElement = document.createElement('div'); // Creates a new, empty <div> element in memory.
    messageElement.classList.add('message', className);
    const p = document.createElement('p'); // Creates a new, empty <p> (paragraph) element.
    p.textContent = message; // Sets the text inside the <p> element to the message string.
    messageElement.appendChild(p); //  Puts the <p> element inside the <div> element. The structure is now <div><p>message text</p></div>.
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
