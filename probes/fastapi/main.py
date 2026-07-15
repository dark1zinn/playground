from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, World!"

@app.post("/math")
async def doMath():
    return 2 + 2
