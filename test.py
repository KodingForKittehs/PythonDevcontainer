import requests

def get_stuff():
    url = 'https://github.com/KodingForKittehs/PythonDevcontainer'
    return requests.get(url)

print(get_stuff().text)
