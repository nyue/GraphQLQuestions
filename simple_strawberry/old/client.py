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


query_body = """
{
  books {
    title
    author
  }
}
"""

create_body = """
{
  create {
    title
    author
  }
}
"""

action(body=query_body)
action(body=create_body)
