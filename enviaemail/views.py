from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import json

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
