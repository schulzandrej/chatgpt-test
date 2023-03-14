import os
import openai
import json

# Set up the API client
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"  # GPT-3.5 Turbo

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {'role': 'user', 'content': 'Gib mir eine Liste von allen deutschen Bundekanzlern mit Ihren Dienstjahren, Alter bei Diestnbeginn und den Geburtstag Gib die Daten im json format zurück.'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])