import requests
from requests_toolbelt.utils import dump
import json



url = "https://catfact.ninja/fact"
ml = 80

# removed code below was used for testing
"""""
requests = requests.get(url)   # sends a http request to url
data = dump.dump_all(requests)  # dumps the raw json response 
print(requests.json())  # prints the content of the json response
print(data.decode("utf-8"))  # decodes the raw json data to utf-8 and prints it

with open("test.txt", "w") as test:  # writes the json data to a file (will overwrite anything in the file)
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
