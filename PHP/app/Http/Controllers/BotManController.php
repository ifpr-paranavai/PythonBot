<?php
namespace App\Http\Controllers;
   
use BotMan\BotMan\BotMan;
use Illuminate\Http\Request;
use BotMan\BotMan\Messages\Incoming\Answer;
   
class BotManController extends Controller
{
    public function handle()
    {
        $botman = app('botman');
        
        $botman->hears('{message}', function($botman, $message) {
   
            if ($message == 1) {
                $botman->reply('Claro, você gostaria de fazer uma reserva. Por favor, entre em contato conosco e indique as datas de check-in e check-out, bem como o número de hóspedes.');
            }
            else if ($message == 2) {
                $botman->reply('Temos uma variedade de serviços disponíveis, incluindo restaurante, spa e academia. Posso fornecer mais detalhes sobre algum desses serviços, basta entrar em contato em nosso telefone');
            }
            else if ($message == 3) {
                $botman->reply('Nosso hotel está localizado no centro da cidade, próximo a várias atrações populares. O endereço é Las Vegas city.');
            }
            else if ($message == 4) {
                $botman->reply('O horário de check-in é às 15:00. No entanto, se você precisar de um check-in antecipado, por favor, entre em contato conosco para verificar a disponibilidade.');
            }
            else if ($message == 5) {
                $botman->reply('O horário de checkout é às 12:00. Se você precisar de um checkout tardio, por favor, informe-nos com antecedência para que possamos fazer os arranjos necessários.');
            }
            else if ($message == 6) {
                $botman->reply('Nossos atendentes trabalham das 09 às 18 horas, caso esteja dentro desse período, aguarde um momento!');
            }
            else if ($message == 7) {
                $botman->reply('Nossos telefone para contato é +00(00)00000-0000');
            }
            else{
                $botman->reply("
                    Olá, digite um dos numeros das opções abaixo para que eu possa te auxiliar melhor,
                    Você deseja:
                    <br><br>
                    1 - Fazer uma reserva
                    <br><br>
                    2 - Conhecer nossos serviços
                    <br><br>
                    3 - Informações sobre a localização
                    <br><br>
                    4 - Horário de check-in
                    <br><br>
                    5 - Horário de checkout
                    <br><br>
                    6 - Falar com Atendente
                    <br><br>
                    7 - Contato
                ");
            }
   
        });
   
        $botman->listen();
    }
}
