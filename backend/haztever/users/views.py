import logging
import requests

from django.conf import settings

from django.template.response import TemplateResponse

from dj_rest_auth.registration.views import ConfirmEmailView

class CustomConfirmEmailView(ConfirmEmailView):
    """
    Vista personalizada que hereda de ConfirmEmailView para validar el email
    mientras se construye el frontend
    """
    
    template_name = "account/email_confirmed.html"
    
    def get(self, request, *args, **kwargs):
        key = kwargs.get('key')
        
        try:
            if  settings.IS_LAMBDA:
                base_url = settings.HOST
            else:
                base_url = 'http://127.0.0.1:8000'
            
            verify_url = f"{base_url}/api/auth/registration/verify-email/"
            
            response = requests.post(verify_url, json={'key': key})
            
            if response.status_code == 200:
                return TemplateResponse(
                    request,
                    'account/email_confirmed.html',
                    {
                        'success': True,
                        'message': '¡Tu email ha sido verificado exitosamente! Ya puedes usar tu cuenta.',
                        'user': request.user if request.user.is_authenticated else None
                    }
                )
            else:
                return TemplateResponse(
                    request,
                    'account/email_confirmed.html',
                    {
                        'success': False,
                        'message': 'El enlace de confirmación es inválido o ha expirado. Por favor, solicita un nuevo enlace.'
                    }
                )
                
        except Exception as e:
            return TemplateResponse(
                request,
                'account/email_confirmed.html',
                {
                    'success': False,
                    'message': 'Hubo un error al verificar tu email. Por favor, inténtalo de nuevo más tarde.'
                }
            )
