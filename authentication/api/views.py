from rest_framework.decorators import api_view
from authentication.api.serializer import RegSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from authentication import models
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST',])
def reg_view(request):
    if request.method == 'POST':
        serializer = RegSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
        else:
            data = serializer.errors

        return Response(data)


@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
