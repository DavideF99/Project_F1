##################################### Basic uvicorn #####################################

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Project F1 backend!"}

if __name__ == "__main__":
    uvicorn.run("backend.milestone1:app", host="127.0.0.1", port=5000, log_level="info")

# run in CLI with -> "python -m backend.milestone1"
