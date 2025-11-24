# Backend of Application

from fastapi import FastAPI, Request # Imports main "FastAPI" class for the creation of the web app and "request" gets the info from incoming user requests
from fastapi.responses import HTMLResponse, JSONResponse # "HTMLResponse" sends back html content, "JSONResponse" sends data in JSON format
from fastapi.staticfiles import StaticFiles # used to server static files like CSS, JavaScript, and Images
from fastapi.templating import Jinja2Templates # Allows you to template engines to render HTML pages dynamically

import ollama # Importa ollama
from pydantic import BaseModel # Data validation library, BaseModel is used to define the structures and data types of the data expected to receive in an API request

import uvicorn # For cserver
import logging

# ---- CREATING FastAPI APP ----  #
app = FastAPI()
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# ---- MOUNTING STATIC FILES --- #
'''
 - app.mount() -> Creates a path that doesn't run python code but instead serves files directly from the "/static" dir.
                  This is the URL path.
                  When your browser requests http://127.0.0.1:8000/static/script.js, FastAPI knows to look in the static files directory.

 - StaticFiles(...) -> This tells FastAPI that for any request starting with "/static", it should find the corresponding file inside
                       "directory=..." path.
'''
app.mount("/static", StaticFiles(directory="fast_api_chatbot/static"), name="static")

# ---- SETTING UP TEMPLATES ---- #
'''
- templates -> Configures the Jinja2 template engine.
               Tells the application that all HTML template files are located in the directory defined.
'''

templates = Jinja2Templates(directory="fast_api_chatbot/templates")

# ---- DEFINING THE REQUEST DATA SHAPE ---- #
'''
- This is a Pydantic model
- Tells FastAPI that when a request comes from the "/chat" endpoint, the request's should be a JSON object with a single key named "message"
- Example: {"message": "Hello, world!"}
- FastAPI uses this for automatic data validation and documentation.
'''
class ChatMessages(BaseModel):
    message: str

# ---- DEFINING THE CHAT LOGIC ---- #

'''
- The user will be able to send a prompt to the model phi of ollama and the bot will be able to give a response back
'''
MODEL_NAME = "phi" # Pre-trained model

def chat_with_model(prompt: str):
    response = ollama.chat(
        model = MODEL_NAME,
        messages = [{"role": "user", "content": prompt}]
    )
    return response['message']['content']

# ---- CREATING THE API ROUTES (ENDPOINTS) ---- #
'''
- An API Route is a URL that the server listens to
- The Root Route ('/')
- @app.get("/") -> handles GET requests to the main URL (/, e.g., http://127.0.0.1:8000)
- return templates.TemplateResponse(...) -> finds the 'index.html' file in your templates directory, renders it, and sends it back to the
                                            browser as an HTML response.
                                            The {"request": request} part is required by Jinja2.
'''
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---- THE CHAT ROUTE ('/chat') ---- #
'''
 - @app.post("/chat") -> This tells FastAPI that the chat function should handle POST requests to the /chat URL.
                         POST is used because the browser is sending data (the user's message) to the server.

- chat_message: ChatMessage -> This is where the magic of Pydantic happens.
                               FastAPI automatically takes the body of the POST request, validates it against
                               your ChatMessage model, and gives you a clean chat_message object to work with.

- answer = chat_with_model(chat_message.message) ->  It calls your chat function with the message received from the frontend.

'''
@app.post("/chat")
async def chat(chat_message: ChatMessages):
    try:
        answer = chat_with_model(chat_message.message)
        return JSONResponse(content={"response": answer})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# ---- RUNNING THE APPLICATION ---- #

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                log_level="info"
                )