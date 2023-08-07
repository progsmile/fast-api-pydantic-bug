import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from starlette.responses import Response

from src.user import CreateUserRequestAttr, CreateUserRequestModelConfig

app = FastAPI(openapi_url=None)
router = APIRouter()


@router.post("/user_1")
async def create_user_1(request: CreateUserRequestAttr, response: Response) -> dict:
    response.status_code = 200
    return {"message": "Well done"}


@router.post("/user_2")
async def create_user_2(request: CreateUserRequestModelConfig, response: Response) -> dict:
    response.status_code = 200
    return {"message": "Well done"}


app.include_router(router)


def main() -> None:
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
