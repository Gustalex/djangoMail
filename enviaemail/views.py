from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from decouple import config

# pipenv run python manage.py runserver para rodar o servidor no package.json
# ou fazer um script no package.json para cada sistema operacional e fazer um .sh e um .bat
# "scripts": {
#    "dev:unix": "concurrently \"nodemon serve.js\" \"npm run test\" \"./start_server.sh\"",
#    "dev:win": "concurrently \"nodemon serve.js\" \"npm run test\" \"start_server.bat\"",
#   "test": "jest",
#    "test:watch": "jest --watch"
#}

def envia_email(request):
    subject = "Confirmacao de reserva CIPT"
    message = "Essa e uma mensagem automatica favor nao responder."
    html_message = """
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Regras de Uso das Salas de Estudo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 700px;
            margin: 20px auto;
            padding: 30px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            text-align: center;
            color: #333;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 20px;
            margin-bottom: 15px;
        }
        h3 {
            font-size: 18px;
            margin-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
            padding-left: 20px;
            text-indent: -20px;
        }

        .highlight {
            font-weight: bold;
            color: #d9534f;
        }
        .highlight2 {
            font-weight: bold;
            color: #b6100b;
            text-align: center;
            display: block;
            margin-top: 20px;
        }
        p {
            margin-bottom: 1em;
        }
        img {
            width: 100px;
            display: block;
            margin: 0 auto 20px auto;
        }
        .footer {
            text-align: center;
            color: #888;
            font-size: 12px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.postimg.cc/y6SxCFFC/cipt.png" alt="Centro de Inovação Jaraguá">
        <h1>SUA RESERVA FOI CONFIRMADA! CONFIRA AS REGRAS DE UTILIZAÇÃO:</h1>
        <h2>Regras de Uso das Salas de Estudo</h2>
        <ul>
            <li>➔ As chaves das salas de estudo só podem ser entregues mediante <span class="highlight">reserva prévia</span> e com a presença de no mínimo <span class="highlight">3 pessoas</span> e no máximo <span class="highlight">5 pessoas</span>.</li>
            <li>➔ O tempo máximo de utilização das salas é de <span class="highlight">3 horas</span>.</li>
            <li>➔ Há uma tolerância de <span class="highlight">30 minutos</span> para a retirada da chave. Após esse período, se outro grupo com no mínimo 3 pessoas solicitar a sala, a chave será entregue a eles.</li>
            <li>➔ Se durante o uso da sala o número de pessoas presentes cair para menos de 3, a chave deverá ser devolvida imediatamente.</li>
            <li>➔ Não é permitida a alimentação dentro das salas, assim como em todo o espaço de coworking.</li>
            <li>➔ Mantenha o máximo de silêncio possível ao utilizar o coworking, pois é uma área dedicada à concentração e trabalho.</li>
            <li>➔ É proibido o uso de vapes, cigarros ou qualquer tipo de fumaça dentro das salas e no espaço de coworking.</li>
            <li>➔ Após o uso, mantenha a sala organizada.</li>
        </ul>
        <h2>Agradecemos a sua colaboração!</h2>
        <p class="highlight2">ESSA É UMA MENSAGEM AUTOMÁTICA, FAVOR NÃO RESPONDER!</p>
        <div class="footer">
            Centro de Inovação Jaraguá @ciptalagoas
        </div>
    </div>
</body>
</html>
    """
    from_email = config('EMAIL_HOST_USER')
    to_list = ['alexandresoja2@hotmail.com']

    send_mail(subject, message, from_email, to_list, fail_silently=False, html_message=html_message)

    return HttpResponse('Email enviado com sucesso!')