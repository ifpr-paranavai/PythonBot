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


conversa.train([
    
    # Perguntas Genéricas
    
    'Olá, tudo bem?', 'Eae, tudo certo?',

    'Qual o seu nome?', 'Moya, seu amigo bot',

    'Prazer em te conhecer', 'Igualmente meu querido',

    'Quantos anos você tem?', 'Eu nasci em 2023, faz as contas, rs.',

    'Qual a sua bebida favorita?', 'Eu bebo café, o motor de todos os programas de computador.',

    'Hahahaha', 'kkkk','kkk', 'kkkk',

    'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',

    'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',

    # Perguntas História
    'Quem foi o trigésimo sétimo presidente dos Estados Unidos?','Richard Nixon',

    'Em que ano o presidente John F. Kennedy foi assassinado?','1963',
    
    'Quem foi Steve Jobs?','Steven Paul Jobs foi um inventor, empresário e magnata americano no setor da informática. Notabilizou-se como co-fundador, presidente e diretor executivo da Apple Inc.',
    
    'Quem foi o primeiro homem a pisar na lua?','Neil Alden Armstrong',
    
    'Quem foi o primeiro presidente do Brasil?','Deodoro da Fonseca, em 1889.',
    
    'Quem foi a primeira presidente mulher do Brasil?','Dilma Rousseff, de 2011 a 2016.',
    
    'Quantos estados tem o Brasil?','São 26 estados mais o Distrito Federal.',
    
    'Qual foi a primeira capital do Brasil?','Salvador, de 1549 até 1763.',
      
    # Perguntas Teste de turing
    'O que é o teste de Turing?','O teste de Turing é um teste de inteligência artificial proposto por Alan Turing em 1950 para avaliar a capacidade de uma máquina em exibir comportamento inteligente que é indistinguível do comportamento humano.',
    
    'Como funciona o teste de Turing?','O teste de Turing envolve um avaliador humano que tenta distinguir entre as respostas de uma máquina e as respostas de um ser humano em uma conversa por texto. Se o avaliador não puder distinguir entre as duas, a máquina passa no teste.',
    
    'Qual é o objetivo do teste de Turing?','O objetivo do teste de Turing é determinar se uma máquina pode exibir comportamento inteligente semelhante ao de um ser humano, o que é considerado um marco importante na inteligência artificial.',
    
    'Quem foi Alan Turing e qual foi sua contribuição para o teste de Turing?','Alan Turing foi um matemático e cientista da computação britânico que propôs o teste de Turing como um meio de avaliar a inteligência artificial. Sua contribuição foi pioneira na teoria da computação e na inteligência artificial.',
    
    'O teste de Turing ainda é usado hoje em dia?','Sim, o teste de Turing ainda é usado hoje em dia como um meio de avaliar a capacidade de uma máquina em exibir comportamento inteligente, embora tenha sido criticado por sua validade como um teste de inteligência artificial.',
    
    'O que é o prêmio Loebner e como está relacionado ao teste de Turing?', 'O prêmio Loebner é uma competição anual que oferece um prêmio em dinheiro para o programa de computador que pode enganar a maioria dos avaliadores humanos em uma conversa por texto. A competição está diretamente relacionada ao teste de Turing, pois seu objetivo é criar um programa de computador que possa passar no teste.',    
    
    # Perguntas Inteligência Artificial
    'O que é inteligência artificial?','Inteligência artificial é a capacidade de uma máquina ou computador realizar tarefas que normalmente requerem inteligência humana, como reconhecimento de fala, visão computacional, aprendizado de máquina, entre outras.',
    
    'Como a inteligência artificial é usada atualmente?', 'A inteligência artificial é usada em muitas aplicações, incluindo assistentes virtuais, chatbots, reconhecimento de voz, recomendação de produtos, análise de dados, entre outras.',

    'Qual é a diferença entre inteligência artificial e aprendizado de máquina?','Aprendizado de máquina é uma subárea da inteligência artificial que se concentra no desenvolvimento de algoritmos que permitem que um sistema aprenda a partir de dados, sem ser explicitamente programado para isso.',

    'Quais são os desafios éticos associados à inteligência artificial?', 'Os desafios éticos associados à inteligência artificial incluem privacidade, discriminação algorítmica, segurança cibernética, responsabilidade e transparência.',

    'Quais são as diferenças entre IA forte e IA fraca?', 'IA forte é um tipo de inteligência artificial que pode realizar tarefas que normalmente exigiriam inteligência humana, enquanto a IA fraca é um tipo de inteligência artificial que pode realizar tarefas específicas, mas não pode ser aplicada a outras áreas.',

    'O que é deep learning?', 'Deep learning é uma técnica de aprendizado de máquina que usa redes neurais artificiais profundas para analisar grandes conjuntos de dados e encontrar padrões.',
    
    'Quais são os principais desafios da inteligência artificial?', 'Os principais desafios da inteligência artificial incluem a criação de sistemas mais flexíveis e adaptáveis, garantindo a segurança dos sistemas, aumentando a transparência dos algoritmos e promovendo a responsabilidade ética.',

    'O que é NLP?', 'NLP é a sigla para "Natural Language Processing" (Processamento de Linguagem Natural), que é uma área da inteligência artificial que se concentra na interação entre humanos e computadores usando linguagem natural.',
    
    # Perguntas IFPR
    'Quando foi inaugurado o IFPR campus Paranavaí?', 'O campus Paranavaí do Instituto Federal do Paraná (IFPR) foi inaugurado no dia 23 de setembro de 2013.',
    
    'Quais os cursos de graduação disponíveis no IFPR campus Paranavaí?', 'Cursos de Graduação: Licenciatura em Química, Bacharelado em Agronomia, Engenharia Elétrica, Engenharia de Software',
    
    'Quantos IFPR existem atualmente?', 'Atualmente, o Instituto Federal do Paraná(IFPR) conta com 25 campi em funcionamento, distribuídos em diversas cidades do estado. Além disso, o IFPR possui uma Reitoria, localizada em Curitiba, que é responsável pela gestão e coordenação dos campi.',
    
    'Qual o maior campus do IFPR?', 'O maior campus do IFPR é o campus Curitiba, localizado na cidade de Curitiba, capital do estado do Paraná',

    'Quantos alunos tem todos os campi do IFPR?', 'De acordo com dados de 2021, o Instituto Federal do Paraná (IFPR) possui cerca de 29 mil alunos matriculados em cursos técnicos, de graduação e de pós-graduação, distribuídos entre seus 25 campi.',

    'Quantos alunos tem o IFPR campus Paranavaí?', 'De acordo com o Censo da Educação Superior de 2020, o IFPR campus Paranavaí tem um total de 1.073 alunos matriculados em cursos técnicos, de graduação e de pós-graduação.',
    
    ])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Moya: ", resposta)
        else:
            print("Não manjo dessas paradas :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
