from django.test import TestCase, RequestFactory
from django.core import mail
from enviaemail.views import envia_email
import json

class EmailTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_envia_email(self):
        request = self.factory.post('http://127.0.0.1:8000/email/',
                                    {'subject': 'Teste Subject',
                                    'message': 'Teste Message',
                                    'recipient': 'alexandregustavo00@gmail.com'},
                                    content_type  = 'application/json')
        response = envia_email(request)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content, {'status': 'success', 'message': 'Email enviado com sucesso'})

        #confirma a saida do email
        self.assertEqual(len(mail.outbox),1)
        self.assertEqual(mail.outbox[0].subject, 'Teste Subject')