from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}
