from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

bot = ChatBot(
    'Moya',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch', 
        'chatterbot.logic.MathematicalEvaluation'
    ],

    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)

with open('perguntas.txt', 'r') as arquivo:
    perguntas = arquivo.read().splitlines()

conversa.train(perguntas)

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Moya: ", resposta)
        else:
            print("Não manjo dessas paradas :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
