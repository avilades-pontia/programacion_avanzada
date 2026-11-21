import requests

base_url = "http://localhost:11434/"


# response = requests.post(
#     base_url + "api/generate",
#     json={"model": "qwen3:14b", "prompt": "What is the capital of Spain?"}
# )

# print(response.json())


response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "qwen3:14b", "prompt": "What is the capital of Spain?"}
)

print(response.text)  # Print raw response instead of parsing JSON
print("\n" * 2)
print(response.json())



# response = requests.post(
#     "http://localhost:11434/api/generate",
#     json={"model": "llama3", "prompt": "What is the capital of Spain?"}
# )

# print(response.json())


# response = requests.get("http://localhost:11434/api/ps")

# data = response.json()
# print(type(data))
# if type(data) == dict:
#     print(f"\n{data["value"]}") #json
