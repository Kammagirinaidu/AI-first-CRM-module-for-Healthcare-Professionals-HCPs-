from fastapi import FastAPI
from agent.langgraph_agent import build_agent
from schemas import InteractionCreate

app = FastAPI()
agent = build_agent()

@app.post("/chat")
def chat(input: InteractionCreate):
    return agent.invoke({"input": input.text})