# Basic Chatbot with Ollama

This project provides a simple command-line chatbot that uses Ollama to run a local large language model. It also includes a web-based version of the chatbot built with FastAPI.

## Features

### Basic Chatbot (`main.py`)

*   **Interactive Chat:** A simple, interactive command-line interface to chat with a local large language model.
*   **Model Selection:** Easily configure the model to use by changing the `MODEL_NAME` variable in the script.
*   **Error Handling:** Basic error handling to guide the user on setting up the Ollama service.

### Web Chatbot (`fast_api_chatbot/`)

*   **Web Interface:** A user-friendly web interface for the chatbot, allowing users to interact with the model through a browser.
*   **FastAPI Backend:** Built with the high-performance FastAPI framework, providing a fast and efficient backend.
*   **Asynchronous Processing:** Takes advantage of FastAPI's asynchronous capabilities to handle multiple users and requests efficiently.
*   **Simple and Clean UI:** A clean and simple chat interface styled with CSS.

## Requirements

*   Python 3.6+
*   Ollama
*   `ollama` Python library
*   `Flask`
*   `fastapi`
*   `uvicorn`

You can install the Python libraries using pip:

```bash
pip install ollama Flask fastapi uvicorn
```

## Running the Basic Chatbot

1.  **Start the Ollama Service:** Make sure the Ollama service is running. You can start it by running `ollama serve` in your terminal.

2.  **Download a Model:** Download a model to use with the chatbot. We recommend `phi` for users with limited RAM.

    ```bash
    ollama pull phi
    ```

3.  **Run the script:**

    ```bash
    python3 main.py
    ```

## Running the Web Application (FastAPI)

1.  **Start the Ollama Service:** Make sure the Ollama service is running.

2.  **Download a Model:** Make sure you have a model downloaded, for example `phi`.

3.  **Run the application:**

    ```bash
    python3 fast_api_chatbot/main.py
    ```

4.  **Open in your browser:** Open your web browser and navigate to `http://127.0.0.1:8000`.

## Project Structure

```
.
├── main.py
├── README.md
├── fast_api_chatbot
│   ├── main.py
│   ├── static
│   │   ├── script.js
│   │   └── style.css
│   └── templates
│       └── index.html
```