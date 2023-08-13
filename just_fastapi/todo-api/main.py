from fastapi import FastAPI
from fastapi_graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware

from .database import get_db
from .schema import Query, CreateTodo, UpdateTodo, DeleteTodo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQLApp(schema=Query,
              mutations=[CreateTodo, UpdateTodo, DeleteTodo]))


@app.on_event("startup")
async def startup():
    await get_db.connect()


@app.on_event("shutdown")
async def shutdown():
    await get_db.disconnect()
