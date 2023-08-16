

# we have imported the requests module
import requests
# defined a URL variable that we will be
# using to send GET or POST requests to the API
# url = "http://localhost:8000/graphql"


def action(body: str, url: str = "http://localhost:8000/graphql"):
    response = requests.post(url=url, json={"query": body})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)


add_body = """
mutation {
  addBook(title: "The Little Prince", author: "Antoine de Saint-Exupéry") {
    title
  }
}
"""

delete_body = """
mutation {
  deleteBook(title: "The Little Prince", author: "Antoine de Saint-Exupéry")
}
"""

update_body = """
mutation {
  updateBook(title: "The Little Prince", author: "Antoine de Saint-Exupéry")
}
"""

query_body = """
query {
  hello
}
"""

query_with_args_body = """
query {
  hello(name: "Nicholas")
}
"""

action(body=query_with_args_body)
action(body=query_body)
action(body=add_body)
action(body=delete_body)
action(body=update_body)
