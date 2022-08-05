import requests
from requests_toolbelt.utils import dump
import json



url = "https://catfact.ninja/fact"
ml = 80
"""""
requests = requests.get(url)
data = dump.dump_all(requests)
print(requests.json())
print(data.decode("utf-8"))

with open("test.txt", "w") as test:
    test.write(data.decode("utf-8"))
"""""

i = 0

while 20 > i:  # while i is less than 20
    request = requests.get(url)  # sends a http request to url
    print(request.json())  # prints the returned fact
    cat = json.dumps(request.json())  # dumps the fact to a string
    with open("test.txt", "a") as f:  # appends the string to a text document called "test.txt"
        f.write(cat)
        f.write("\n")
    i += 1  # increments i
