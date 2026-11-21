from ollama import chat
from ollama import ChatResponse
import ollama

ia_model = "qwen3:14b"

response: ChatResponse = chat (
    model = ia_model,
    messages=[
        {
        'role': 'user',
        'content': '1 + 1', 
        },
    ],
)

model_data = ollama.ps()

print(type(model_data))

if model_data == dict:
    print(f"el modelo cargado: {model_data["value"]}")

if type(model_data) == list:
    for category in model_data:
        print(f"\nCategoria: {category}") #list


#print(f"\nrespuesta de ollma:\n{response['message']['content']}")

print(f"el modelo ha tardado en responder: {response.eval_duration / 1e9}")
print(f"el modelo count: {response.eval_count}")
print(f"el modelo usado: {response.model}")
print(f"el modelo ha tardado en cargar: {response.load_duration / 1e9}")
print(f"el modelo tiempo usado: {response.total_duration / 1000000000}")


# or access fields directly from the response object
# print(f"\nrespuesta de ollama:\n{response.message.content}")