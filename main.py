# import time
import uvicorn
from src.infrastructure.dependencies import init_routers
from fastapi import FastAPI

# def main():
#     init_rabbitmq()

app = FastAPI()

init_routers(app)


if __name__ == '__main__':
    # main()
    uvicorn.run("main:app", host="0.0.0.0", port=8087, reload=True)
    # while True:
    #     time.sleep(1)
