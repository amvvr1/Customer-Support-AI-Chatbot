from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import agent
from pydantic import BaseModel

class Request(BaseModel):
    message : str 
    thread_id: str = "1"

app = FastAPI()
    
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/chat")
def chat(request: Request):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": request.message}]},
        {"configurable": {"thread_id": request.thread_id}}
    )
    
    return {"response": response["messages"][-1].content}