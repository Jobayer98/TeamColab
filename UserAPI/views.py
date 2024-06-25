from rest_framework.decorators import api_view, APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema

from .models import CustomUser as User
from .serializers import RegistrationSerializer, UserSerializer

@swagger_auto_schema(method='post', request_body=RegistrationSerializer)
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


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = [JSONParser]
    
    def get(self, request, *args, **kwargs):
        try:
            print(request.header)
            user = User.objects.get(id=kwargs['id'])
            if request.user.id == user.id:
                return Response({
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'date_joined': user.date_joined
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error-msg': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error-msg': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['id'])
            if request.user.id == user.id:
                user.username = request.data.get('username', user.username)
                user.password = request.data.get('password', user.password)
                user.first_name = request.data.get('first_name', user.first_name)
                user.last_name = request.data.get('last_name', user.last_name)
                user.email = request.data.get('email', user.email)
                user.save()
                return Response({'success': 'User updated successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error-msg': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error-msg': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['id'])
            if request.user.id == user.id:
                user.delete()
                return Response({'success': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error-msg': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error-msg': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
