# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email', 'uniqueNumberForTeacher', 'haveTeacher', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')
#         print(password,"              ",email)
#         user = authenticate(email=email, password=password)
#         if not user:
#             raise serializers.ValidationError('Invalid login credentials')
#         data['user'] = user
#         return data
from rest_framework import serializers
from .models import Image, Quiz, SchoolUser
from django.contrib.auth.hashers import make_password

# class SchoolUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SchoolUser
#         fields = '__all__'

# class SchoolUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = SchoolUser
#         fields = '__all__'

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         validated_data['password'] = make_password(password)
#         user = SchoolUser.objects.create(**validated_data)
#         return user
class SchoolUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = SchoolUser
        fields = '__all__'

        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
    context = serializers.CharField(required=False)