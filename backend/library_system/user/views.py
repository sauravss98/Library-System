from django.shortcuts import render,get_object_or_404
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserAuthSerializer
from .models import User

# Create your views here.

""" 
User Authentication and Token System
"""

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User , email = request.data['email'])
    if not user.check_password(request.data["password"]):
        return Response({"detail":"Not found"}, status= status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserAuthSerializer(instance=user)
    return Response({"token":token.key,"user_email":serializer.data['email'],"status":status.HTTP_201_CREATED})

@api_view(['POST'])
def signup(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(email = request.data['email'])
        # if(user):
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user = user)
        return Response({"token":token.key,"user":serializer.data})
        # else:
        #     user = User.objects.create(email = request.data['email'])
        #     user.set_password(request.data["password"])
        #     user.save()
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))

class UserLogout(APIView):
    def post(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)