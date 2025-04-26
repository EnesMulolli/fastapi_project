from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/greet/")
def read_root(name: str):
    return{"message": f"Hello, {name}!"}

@app.get("/items")
def read_items():
    return {"items":["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

print(1)