from rest_framework.decorators import api_view
from authentication.api.serializer import RegSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from authentication import models


@api_view(['POST',])
def reg_view(request):
    if request.method == 'POST':
        serializer = RegSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)
