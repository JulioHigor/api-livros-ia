import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Chave encontrada:", api_key is not None)

client = genai.Client(api_key=api_key)

print("Cliente Gemini criado!")

resposta = client.interactions.create(
    model="gemini-3.5-flash",
    input="Responda apenas: Funcionou!"
)

print("Resposta do Gemini:")
print(resposta.output_text)