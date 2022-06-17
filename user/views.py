# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import User


class UserView(APIView): # CBV 방식
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        return Response({'message': 'get method!!'})
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})





class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # 회원가입
    def post(self, request):
        user_type = request.data.get('user_type', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        User.objects.create_user(user_type=user_type, email=email, password=password)
        return Response({"message": "회원가입 성공!!"})
    
    # 회원가입 몰라