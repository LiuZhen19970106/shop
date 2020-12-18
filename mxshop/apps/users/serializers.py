from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, min_length=4)

    def validate_code(self, code):
        pass

    class Meta:
        model = User
        fileds = ("username", "code", "mobile")
