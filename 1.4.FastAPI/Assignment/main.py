from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from datetime import datetime
import database

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    status: int

@app.get("/")
def read_root():
    return "Hi! Welcome to my API."

@app.post("/save", status_code=status.HTTP_201_CREATED, tags=["tasks"])
async def save_task(task: Task):
    try:
        created_time = datetime.now().isoformat()
        database.add_task(task.title, task.description, task.status, created_time)
        return {"message": "Task added!", "time": created_time.isoformat()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/list")
async def list_tasks():
    tasks = database.get_all_tasks()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found!")
    return tasks

@app.get("/find/{id}")
def find_task(id: int):
    task = database.find_task(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found!")
    return task

@app.put("/update/{id}")
async def update_task(id: int, task: Task):
    if not database.find_task(id):
        raise HTTPException(status_code=404, detail="Task not found!")
    try:
        database.update_task(id, task.title, task.description, task.status)
        return "Task updated!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete/{id}")
def delete_task(id: int):
    if not database.find_task(id):
        raise HTTPException(status_code=404, detail="Task not found!")
    try:
        database.delete_task(id)
        return "Task deleted!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

