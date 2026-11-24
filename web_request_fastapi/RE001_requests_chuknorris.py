import requests

'''
get https://api.chuknorris.io/jokes/random


get https://api.chuknorris.io/jokes/random?category={category}

get https://api.chuknorris.io/jokes/categories

["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]

get https://api.chuknorris.io/jokes/search?query={query}
'''


base_url = 'https://api.chucknorris.io/jokes/'

category = 'political'
url_random_joke = base_url + 'random'
url_categories = base_url + 'categories'
url_selected_category = base_url + 'random?category=' + category

response = requests.get(url_selected_category)

if response.status_code == 200:
    data = response.json()
    
    if type(data) == dict:
        print(f"\n{data["value"]}") #json
    # data = response.iter_lines
    
    if type(data) == list:
        for category in data:
            print(f"\nCategoria: {category}") #list
    # print(f"\n{response}\n")
    # print(f"\n{data}\n")
    # print(f"codigo http: {response.status_code}\n")
    # print(f"\n{response}\n")
    print(f"\nheaders: {response.headers}\n")
    print(f"\nElapsed: {response.elapsed}\n")
else:
    print(f"\nError al obetener datos: {response.status_code}\n")