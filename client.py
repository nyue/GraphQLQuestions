# we have imported the requests module
import requests
# defined a URL variable that we will be
# using to send GET or POST requests to the API
url = "http://localhost:8000/graphql"
 
body = """
{
  books {
    title
    author
  }
}
"""
 
response = requests.post(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("response : ", response.content)