import openai

openai.api_key = 'sua_chave'

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def main():
    print("Bem-vindo ao ChatBot! Digite 'sair' para encerrar.")
    
    while True:
        pergunta = input("Você: ")
        
        if pergunta.lower() == "sair":
            print("Até logo!")
            break
        
        resposta = get_completion(pergunta)
        print("Bot:", resposta)

if __name__ == "__main__":
    main()
