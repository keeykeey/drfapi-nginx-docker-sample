from .models import CustomUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=20,
        validators = [
            UnicodeUsernameValidator(),
            MinLengthValidator(8),
            UniqueValidator(queryset=CustomUser.objects.all())
            ]
        )

    email = serializers.EmailField(
        validators = [
            UniqueValidator(queryset = CustomUser.objects.all())
        ]
    )

    password = serializers.CharField(
        validators = [
            MinLengthValidator(8)
            ]
    )

    class Meta:
        model = CustomUser
        fields = ("id","username", "email","password")
        extra_kwargs = {
            'password':{'write_only':True,'required':True},
        }

    def create(self,validated_data):
        customUser = CustomUser.objects.create_user(**validated_data)
        return customUser
