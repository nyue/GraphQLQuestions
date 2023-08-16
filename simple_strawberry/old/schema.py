import typing
import strawberry


@strawberry.type
class Book:
    title: str
    author: str


def get_books():
    print('XXXXXXXXXXXXXX get_books')
    return [
        Book(title='The Great Gatsby (Nicholas)',
             author='F. Scott Fitzgerald (Nicholas)')
    ]


def add_book():
    print('XXXXXXXXXXXXXX add_book')
    return Book(title='The Great Gatsby (Nicholas)',
                author='F. Scott Fitzgerald (Nicholas)')


def update_book():
    print('XXXXXXXXXXXXXX update_book')
    return True


def delete_book():
    print('XXXXXXXXXXXXXX delete_book')
    return True


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


@strawberry.type
class Mutation:
    create: Book = strawberry.field(resolver=add_book)
    update: bool = strawberry.field(resolver=update_book)
    delete: bool = strawberry.field(resolver=delete_book)


schema = strawberry.Schema(query=Query, mutation=Mutation)
