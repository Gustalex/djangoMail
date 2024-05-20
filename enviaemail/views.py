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
    subject = "Confirmacao de reserva"
    message = "Essa e uma mensagem automatica favor nao responder."
    html_message = """
    <html>
    <body>
        <p>Essa e uma mensagem automatica favor nao responder. A sua reserva de sala no CIPT  foi confirmada com sucesso! Confira abaixo as normas de utilizacao:</p>
        <p>ablueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblueblue</p>
    </body>
    </html>
    """
    from_email = config('EMAIL_HOST_USER')
    to_list = ['alexandregustavo00@gmail.com']

    send_mail(subject, message, from_email, to_list, fail_silently=False, html_message=html_message)

    return HttpResponse('Email enviado com sucesso!')