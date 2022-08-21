import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/{value}")
def read_root(value: str = ''):
    return {"Hello": value}


if __name__ == '__main__':
    uvicorn.run(app=app)
