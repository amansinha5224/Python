'''
Request Module in Python:-
    - The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
'''

import requests 
from bs4 import BeautifulSoup

url = "https://indianexpress.com/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)


# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'aman',
#     "body": 'sinha',
#     "userId": 25,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)