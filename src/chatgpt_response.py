import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega .env
load_dotenv()

# OpenAI usando a chave do .env
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_chatgpt_response(texto):    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'user', 'content': texto}
        ]
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    texto = 'Quais são as características da linguagem de programação Python?'
    #resposta = get_chatgpt_response(texto)
    resposta = resposta = (
    'Python é uma linguagem de programação de alto nível, '
    'interpretada, com sintaxe simples e fácil leitura. '
    'Ela é muito utilizada em desenvolvimento web, '
    'ciência de dados, inteligência artificial e automação.'
)


    print("\nRESPOSTA DO CHATGPT:\n")
    print(resposta)
