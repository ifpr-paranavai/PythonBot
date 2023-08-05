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
    # Escopo Bellagio Hotel - Las Vegas

    # Conversas iniciais
    'Olá', 'Seja bem vindo ao Hotel Bellagio, como posso ajudar?',
    'Qual o seu nome?', 'Me chamo Moya e estou a disposição para te ajudar?'
    'Certo, obrigado', 'Ajudo em algo mais?',
    'Não, obrigado', 'Certo, ficamos a disposição',
    'Qual o telefone de vocês?', 'Nosso telefone é (xx)xxxx-xxxx, e nosso atendimento por telefone é 24 horas',
    'Qual o site de vocês?', 'Nosso site é o www.hotelbellagiolasvegas.com',

    # Reservas de hotel e acomodações
    'Desejo fazer uma reserva', 'Certo, para qual dia seria?',
    'Para qual dia vocês tem disponibilidade?', 'Para amanhã se desejar, sera para uma ou mais pessoas?',
    'Para 3 pessoas, qual seria o valor do quarto?','Estamos hoje com a promoção de $5,200 por $4,500 em nossa suíte',
    'Deixa, está muito caro', 'Entendo, se desejar podemos parcelar em até 3x'
    'Posso reservar um quarto para amanhã?', 'Infelizmente só temos vagas a partir de segunda-feira que vem, estamos com muitos eventos na cidade.',
    'Pode ser na segunda então','Certo, para solteiro ou casal?',
    'Solteiro, qual seria o valor?', 'A diária está $1,700.',
    'Vocês parcelam esse valor?','Sim, em até 3x sem juros.',
    'Pode reservar então', 'Certo, poderia me passar seu nome?',
    'Gabriel Moya Nascimento', 'Certo já reservei um quarto em seu nome, algo mais?',
    'Quais tipos de acomodações vocês oferecem?','Oferecemos uma variedade de acomodações, incluindo quartos individuais, duplos, suítes e opções para famílias. Todas as nossas acomodações são confortáveis e bem equipadas para garantir uma estadia agradável.',
    'Como posso fazer uma reserva?',' Fazer uma reserva é simples! Basta fornecer suas datas de check-in e check-out, o número de hóspedes e qualquer preferência especial que você tenha. Se desejar, posso encaminhá-lo para o nosso site seguro de reservas.'
    'Quais são as opções de pagamento disponíveis?','Aceitamos diversas formas de pagamento, incluindo cartões de crédito, transferências bancárias e pagamento em dinheiro no momento do check-in. Você também pode optar por garantir sua reserva com um cartão de crédito e efetuar o pagamento no hotel.',
    'Posso fazer alterações ou cancelar minha reserva?','Claro! Entendemos que planos podem mudar. Você pode fazer alterações em sua reserva ou cancelá-la dentro das políticas de cancelamento do hotel. ',
    'Quais são os horários de check-in e check-out?','Nosso horário padrão de check-in é às 14h e o check-out é até às 12h. Caso precise de um check-in antecipado ou de um check-out tardio, por favor, entre em contato conosco, e faremos o possível para acomodar suas necessidades.',

    # Recomendações personalizadas
    'Quais são as principais atrações turísticas próximas ao hotel?','O hotel Bellagio está localizado em uma área privilegiada, próximo a várias atrações populares, como a Fonte do Bellagio, o Museu de Belas Artes de Bellagio e o Shopping Via Bellagio. Além disso, nossa equipe de concierge pode fornecer mais informações sobre passeios e excursões na região.',
    'Onde posso encontrar restaurantes de alta qualidade nas proximidades?','Temos várias opções gastronômicas premiadas dentro do hotel Bellagio, como os restaurantes Le Cirque e Picasso. Se você estiver interessado em explorar restaurantes externos, recomendamos os restaurantes renomados localizados na Las Vegas Strip, a uma curta caminhada do hotel.',
    'Que atividades de lazer o hotel oferece?','O hotel Bellagio oferece diversas atividades de lazer, incluindo nossas famosas piscinas, o luxuoso spa e tratamentos de bem-estar, além de opções para compras de alto padrão. Também podemos providenciar reservas para apresentações do Cirque du Soleil, que acontecem em nosso teatro exclusivo.',
    'Quais são as opções de entretenimento noturno disponíveis no hotel?',' À noite, você pode aproveitar nossa ampla variedade de entretenimento, incluindo shows no teatro do hotel, apresentações musicais ao vivo em nossos lounges, bem como a oportunidade de desfrutar da vida noturna animada da Las Vegas Strip.',
    'Existe algum serviço especial para hóspedes em lua de mel?','Sim, oferecemos pacotes especiais para hóspedes em lua de mel, que incluem comodidades adicionais e experiências românticas para tornar sua estadia inesquecível. Nossa equipe de concierge terá prazer em ajudá-lo a personalizar sua experiência conforme suas preferências.',
    'Quais são as atrações turísticas recomendadas para famílias?','Para famílias, recomendamos visitar o Shark Reef Aquarium no Mandalay Bay, o High Roller na The LINQ, e o Adventure Dome no Circus Circus. Todas essas atrações são ideais para todas as idades e proporcionam diversão para toda a família.',
    'Quais atividades ao ar livre estão disponíveis nas proximidades?','Se você gosta de atividades ao ar livre, pode explorar as belas paisagens do Red Rock Canyon National Conservation Area, fazer passeios de helicóptero sobre a Las Vegas Strip ou fazer trilhas no Mt. Charleston, todos localizados a uma curta distância de carro do hotel.',
    
    # Promoções e ofertas especiais: 
    'Existem promoções ou pacotes especiais disponíveis para reservas?','Sim, temos promoções e pacotes especiais disponíveis durante diferentes períodos do ano. Essas ofertas podem incluir descontos em estadias prolongadas, pacotes com refeições inclusas ou experiências exclusivas. Para saber mais, posso verificar as ofertas atuais para suas datas de viagem.',
    'Há alguma oferta especial para hóspedes em lua de mel ou ocasiões especiais?','Sim, temos pacotes especiais para hóspedes em lua de mel, aniversários e outras ocasiões especiais. Esses pacotes podem incluir amenidades especiais, como decoração romântica no quarto, champanhe e tratamentos de spa. Você pode escolher um pacote pré-definido ou personalizar sua experiência.',
    'Como posso receber notificações sobre as ofertas e promoções do hotel?',' Para receber notificações sobre nossas ofertas e promoções especiais, você pode se inscrever em nossa newsletter por e-mail. Além disso, você pode seguir nossas redes sociais e verificar regularmente nosso site para ficar atualizado sobre as últimas ofertas.',
    'Existem descontos especiais para membros de programas de fidelidade?','Sim, temos benefícios exclusivos para membros de nosso programa de fidelidade. Os membros podem receber descontos adicionais em suas estadias, acumular pontos para resgatar prêmios e receber ofertas personalizadas com base em suas preferências de viagem.',
    'Posso obter um desconto ao reservar diretamente no site do hotel?','Sim, ao reservar diretamente em nosso site oficial, você pode receber descontos exclusivos e garantir as melhores tarifas disponíveis. Nossa equipe de reservas está disponível para ajudá-lo durante o processo de reserva.',

    # Suporte durante a estadia
    'Como posso entrar em contato com a recepção ou a equipe de concierge durante minha estadia?', 'Durante sua estadia, você pode entrar em contato com nossa equipe de recepção e concierge através do telefone do quarto ou visitando a recepção localizada no lobby do hotel. Se preferir, também pode utilizar o chat do nosso aplicativo para dispositivos móveis para obter assistência.',
    'Preciso de mais toalhas e roupas de cama extras no quarto. Como posso solicitar isso?',' Ficamos felizes em atender às suas necessidades. Você pode solicitar mais toalhas e roupas de cama extras diretamente pelo chat do aplicativo do hotel ou entrando em contato com nossa equipe de serviço de quarto através do telefone do quarto.',
    'Onde posso encontrar informações sobre as comodidades e serviços oferecidos pelo hotel?','Todas as informações sobre as comodidades e serviços oferecidos pelo hotel Bellagio podem ser encontradas no nosso aplicativo para dispositivos móveis ou no material informativo disponível em seu quarto.',
    'Preciso reservar um serviço de transporte para o aeroporto ou outros locais. O hotel pode me ajudar com isso?','Sim, o hotel Bellagio pode ajudá-lo a organizar serviços de transporte para o aeroporto ou outros locais. Entre em contato com a recepção ou utilize o chat do aplicativo para solicitar assistência com a reserva do serviço de transporte.',
    'Gostaria de reservar uma mesa em um dos restaurantes do hotel. Como posso fazer isso?',' Fazer uma reserva em um de nossos restaurantes é fácil. Você pode reservar diretamente pelo chat do aplicativo ou entrar em contato com a recepção para solicitar a reserva em seu nome. Nossa equipe ficará feliz em ajudá-lo.',
    'Vocês aceitam animais?', 'Aceitamos apenas animais domésticos, como cachorro, gato, só não me venha com aranhas, tenho fobia hehehe',
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