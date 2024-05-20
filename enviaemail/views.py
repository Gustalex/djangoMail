from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import json

# pipenv run python manage.py runserver para rodar o servidor no package.json
# ou fazer um script no package.json para cada sistema operacional e fazer um .sh e um .bat
# "scripts": {
#    "dev:unix": "concurrently \"nodemon serve.js\" \"npm run test\" \"./start_server.sh\"",
#    "dev:win": "concurrently \"nodemon serve.js\" \"npm run test\" \"start_server.bat\"",
#   "test": "jest",
#    "test:watch": "jest --watch"
#}

@csrf_exempt
def envia_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject = data['subject']
        message = data['message']
        recipient = data['recipient']

        email = EmailMessage(
            subject = subject,
            body = message,
            from_email = config('EMAIL_HOST_USER'),
            to = [recipient]
        )
        email.content_subtype = 'html'

        try:
            email.send()
            return JsonResponse({'status': 'success','message': 'Email enviado com sucesso'}, status = 200)
        except Exception as e:
            return JsonResponse({'status': 'fail', 'message':str(e)}, status = 500)
        
    return JsonResponse({"message": 'Request invalido'}, status = 400)
