from rest_framework.decorators import api_view
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser as User
from .serializers import RegistrationSerializer, UserSerializer

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
            refresh = RefreshToken.for_user(user)
            token = {
                "token": {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
            }
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def login_view()


class UserView(views.APIView):
    pass