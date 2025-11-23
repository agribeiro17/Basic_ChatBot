# fast_api_chatbot/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import ollama
from pydantic import BaseModel

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="fast_api_chatbot/static"), name="static")

# Templates
templates = Jinja2Templates(directory="fast_api_chatbot/templates")

# Model for request body
class ChatMessage(BaseModel):
    message: str

# Choose the model you pulled, e.g., 'phi'
MODEL_NAME = "phi"

def chat_with_model(prompt: str):
    """
    Send a user prompt to the local Ollama model and get a response.
    """
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return response['message']['content']

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(chat_message: ChatMessage):
    try:
        answer = chat_with_model(chat_message.message)
        return JSONResponse(content={"response": answer})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
