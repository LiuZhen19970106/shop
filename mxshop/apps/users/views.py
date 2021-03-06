from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

User = get_user_model()

# Create your views here.
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """