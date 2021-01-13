from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, status
# Create your views here.
from api.models import User, Employee
from api.serializer import UserModelSerializer, EmployeeModelSerializer


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        password = request.query_params.get('password')

        user_obj = User.objects.filter(username=username, password=password).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return Response({"results": data, "message": True}, status=status.HTTP_200_OK)

        return Response({"results": "登录参数有误", "message": False}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        """
        用户的注册请求
        :param request:
        """
        data = request.data
        serializer = UserModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()

        return Response({"results": UserModelSerializer(user_obj).data})


class EmployeeAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print('pk',pk)
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print(request.data)
        return self.destroy(request, *args, **kwargs)