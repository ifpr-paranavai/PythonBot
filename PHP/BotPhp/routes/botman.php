<?php
use App\Http\Controllers\BotManController;

$botman = resolve('botman');

$botman->hears('Hi', function ($bot) {
    $bot->reply('Hello!');
});

//PERGUNTAS TURING
$botman->hears('O que é o teste de Turing?', function ($bot) 
{ 
    $bot->reply('O teste de Turing é um teste que avalia a capacidade de uma máquina exibir um comportamento inteligente semelhante ao de um ser humano.'); 
});

$botman->hears('Quem inventou o teste de Turing?', function ($bot) 
{ 
    $bot->reply('O teste de Turing foi proposto pelo matemático e filósofo britânico Alan Turing, em 1950.'); 
});

$botman->hears('Qual é o objetivo do teste de Turing?', function ($bot) 
{ 
    $bot->reply('O objetivo do teste de Turing é determinar se uma máquina pode ou não exibir um comportamento inteligente semelhante ao de um ser humano.'); 
});

$botman->hears('Como funciona o teste de Turing?', function ($bot) 
{ 
    $bot->reply('O teste de Turing é baseado em uma conversa entre uma máquina e um ser humano, que deve determinar se as respostas da máquina são ou não indistinguíveis das respostas de um ser humano.'); 
});

$botman->hears('O que é o jogo da imitação?', function ($bot) 
{ 
    $bot->reply('O jogo da imitação é outra forma de se referir ao teste de Turing, em que uma máquina deve imitar o comportamento humano para ser considerada inteligente.'); 
});

$botman->hears('O teste de Turing é usado em quais áreas?', function ($bot)
 {
    $bot->reply('O teste de Turing é usado em áreas como inteligência artificial, ciência da computação, filosofia e psicologia.'); 
});

$botman->hears('Qual é a importância do teste de Turing?', function ($bot)
{ 
    $bot->reply('O teste de Turing é importante porque ajuda a entender as capacidades e limitações das máquinas, bem como a definir o que é inteligência artificial.'); 
});

$botman->hears('Quais são as críticas ao teste de Turing?', function ($bot)
{
    $bot->reply('Algumas críticas ao teste de Turing incluem a falta de critérios precisos para determinar se uma máquina é ou não inteligente, além de não levar em conta outros aspectos da inteligência, como a criatividade.'); 
});

// PERGUNTAS IFPR

$botman->hears('Qual é o endereço do IFPR campus Paranavaí?', function ($bot) {
    $bot->reply('O endereço do IFPR campus Paranavaí é Rua José Feliciano de Oliveira, 331 - Jardim Morumbi, Paranavaí - PR, CEP 87707-780.');
});

$botman->hears('Quais cursos são oferecidos pelo IFPR campus Paranavaí?', function ($bot) {
    $bot->reply('O IFPR campus Paranavaí oferece os cursos técnicos integrados em Agropecuária, Informática e Meio Ambiente, além dos cursos superiores de Tecnologia em Análise e Desenvolvimento de Sistemas e Licenciatura em Computação.');
});

$botman->hears('Quais são as principais atividades extracurriculares do IFPR campus Paranavaí?', function ($bot) {
    $bot->reply('O IFPR campus Paranavaí oferece diversas atividades extracurriculares, como eventos culturais, esportivos, projetos de pesquisa e extensão, palestras e workshops.');
});

$botman->hears('Qual é o telefone de contato do IFPR campus Paranavaí?', function ($bot) {
    $bot->reply('O telefone de contato do IFPR campus Paranavaí é (44) 3424-6700.');
});

$botman->hears('Qual é o horário de funcionamento do IFPR campus Paranavaí?', function ($bot) {
    $bot->reply('O IFPR campus Paranavaí funciona de segunda a sexta-feira, das 8h às 22h, e aos sábados, das 8h às 12h.');
});

$botman->hears('Qual é a história do IFPR campus Paranavaí?', function ($bot) {
    $bot->reply('O IFPR campus Paranavaí foi criado em 2008, a partir da expansão da rede federal de educação profissional e tecnológica. Desde então, tem oferecido ensino de qualidade e formado profissionais capacitados para o mercado de trabalho.');
});

$botman->hears('O IFPR campus Paranavaí possui laboratórios de informática?', function ($bot) {
    $bot->reply('Sim, o IFPR campus Paranavaí possui diversos laboratórios de informática


$botman->hears('Start conversation', BotManController::class.'@startConversation');
