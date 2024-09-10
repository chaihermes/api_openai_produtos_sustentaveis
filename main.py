from openai import OpenAI
from dotenv import load_dotenv
import os

#ler as chaves de acesso
load_dotenv()
# conexão via api com o nosso projeto
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Podemos trocar mensagens com a OpenAi
resposta = cliente.chat.completions.create(
  messages=[
    {
      "role":"system",
      "content":"Listar apenas os nomes dos produtos, sem considerar descrição."
    },
    {
      "role":"user",
      "content":"Liste 3 produtos sustentáveis"
    }
  ],
  model="gpt-4"
)

print(resposta.choices[0].message.content)