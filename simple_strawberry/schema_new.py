import strawberry


@strawberry.type
class Book:
    title: str
    author: str


# Reader, you can safely ignore Query in this example, it is required by
# strawberry.Schema so it is included here for completeness
@strawberry.type
class Query:
    @strawberry.field
    def hello() -> str:
        return "world"

    @strawberry.field
    def hello(name:str) -> str:
        return f'hello with name = "{name}"'


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f"Adding {title} by {author}")

        return Book(title=title, author=author)

    @strawberry.mutation
    def delete_book(self, title: str, author: str) -> bool:
        print(f"Deleting {title} by {author}")

        return True

    @strawberry.mutation
    def update_book(self, title: str, author: str) -> bool:
        print(f"Updating {title} by {author}")

        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
