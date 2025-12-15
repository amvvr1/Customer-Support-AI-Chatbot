from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tools import tools
from pydantic import BaseModel
from langgraph.checkpoint.memory import InMemorySaver
from tools import llm
from langchain.agents import create_agent


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

with open("system_prompt.txt", "r") as f:
    prompt = f.read()


agent = create_agent(llm, tools = tools, system_prompt = prompt, checkpointer=InMemorySaver())

@app.post("/chat")
def chat(request: Request):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": request.message}]},
        {"configurable": {"thread_id": request.thread_id}}
    )
    
    return {"response": response["messages"][-1].content}