#uvicorn main:app --host 127.0.0.1 --port 3000 --reload
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(sentence):
    return {"response" : sentence}

#running fastapi on the port we want
if __name__ == "__main__":
    #main is the name of the file
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)

#to work, it should be called this way: 
#   python3 main.py     on the vm
#   main.py             on local
#if there is an error, for any reason: 
#   uvicorn main:app --port 3000 --reload
