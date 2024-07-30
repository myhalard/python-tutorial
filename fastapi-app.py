from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def get_root():
    return {"service": "fastapi-app", "version": "0.0.1"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "item_name": "an item"}


@app.post("/items")
def create_item(item: dict):
    return {"item": item, "status": "created"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item, "status": "updated"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "status": "deleted"}


def run_server():
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")


if __name__ == "__main__":
    run_server()
