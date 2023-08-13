from fastapi import FastAPI
# This is the GraphQL route handler from the package we created
from graphql_server import graphql_app

app = FastAPI()
# Add the `/graphql` route and set `graphql_app` as its route handler
app.include_route(graphql_app, prefix='/graphql')
