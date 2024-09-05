from rest_framework import generics
from apps.users.models import User
from apps.users.serializers import UserSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
