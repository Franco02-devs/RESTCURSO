from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(object):
    user= None
    user_token_expired=False
    
    def get_user(self,request):
        token=get_authorization_header(request).split()
        if token:
            try:
                token=token[1].decode()
            except:
                return None
            
            token_expire=ExpiringTokenAuthentication()  
            
            user = token_expire.authenticate_credentials(token)
            if user != None and token !=None:
                self.user= user
                return user  
                  
        return None
    
    def dispatch(self, request, *args, **kwargs):
        user= self.get_user(request)
        if user is not None:
            return super().dispatch(request, *args, **kwargs)

        response= Response({'error': ' Se requiere iniciar sesión',
                            },status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer= JSONRenderer()
        response.accepted_media_type ='application/json'
        response.renderer_context = {}
        return response