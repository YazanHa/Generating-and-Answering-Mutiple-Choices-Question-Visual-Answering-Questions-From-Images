# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import login
# from .models import CustomUser
# from .serializers import UserSerializer, LoginSerializer

# class RegisterTeacherView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         serializer.save(uniqueNumberForTeacher=self.request.data.get('uniqueNumberForTeacher'))

# class RegisterStudentView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         teacher_id = self.request.data.get('haveTeacher')
#         teacher = CustomUser.objects.get(uniqueNumberForTeacher=teacher_id)
#         serializer.save(haveTeacher=teacher)

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response({'message': 'Logged in successfully'})

##############################################



# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Image, Quiz, SchoolUser
# from .serializers import ImageSerializer, QuizSerializer, SchoolUserSerializer

# @api_view(['POST'])
# def create_school_user(request):
#     if request.method == 'POST':
#         serializer = SchoolUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_image(request):
#     if request.method == 'POST':
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_all_images(request):
#     if request.method == 'GET':
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)

# @api_view(['POST'])
# def create_quiz(request):
#     if request.method == 'POST':
#         serializer = QuizSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_quizzes_by_image(request, image_id):
#     if request.method == 'GET':
#         quizzes = Quiz.objects.filter(image_id=image_id)
#         serializer = QuizSerializer(quizzes, many=True)
#         return Response(serializer.data)



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image, Quiz, SchoolUser
from .serializers import ImageSerializer, QuizSerializer, SchoolUserSerializer, ImageUploadSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .utils import *
import tempfile
import os
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView


@api_view(['POST'])
def create_school_user(request):
    if request.method == 'POST':
        serializer = SchoolUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_teachers(request):
    if request.method == 'GET':
        schoolUser = SchoolUser.objects.filter(relatedTeacherNumber__isnull = True)
        serializer = SchoolUserSerializer(schoolUser, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_image(request):
    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_images(request):
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_quiz(request):
    if request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_quizzes_by_image(request, image_id):
    if request.method == 'GET':
        quizzes = Quiz.objects.filter(image_id=image_id)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_images_by_teacher(request, teacher_id):
    if request.method == 'GET':
        images = Image.objects.filter(teacher_id=teacher_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
        

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({'error': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = SchoolUser.objects.get(email=email)
    except SchoolUser.DoesNotExist:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


    if not check_password(password, user.password):
        return Response({'error': 'Invalid credentials. p '}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    schoolUser = SchoolUser.objects.filter(email=email)
    serializer = SchoolUserSerializer(schoolUser, many=True)
    
    return Response({
        'id': serializer.data[0]['id'],
        'relatedTeacherNumber': serializer.data[0]['relatedTeacherNumber'],
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_200_OK)



class ImageToMCQsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            context = serializer.validated_data.get('context', '')

            # Save the uploaded image to a temporary location
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                for chunk in image.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name
            
            description = image_to_text(tmp_path)
            
            # Clean up the temporary file
            os.remove(tmp_path)

            strategy_a = TextToMCQsStrategyA()
            strategy_b = TextToMCQsStrategyB()
            strategies = TextToMCQsContext(strategy_a, strategy_b)


            questions_dict = strategies.text_to_mcqs(description, context=context)
            
            # questions_dict = groq_text_to_mcqs(description, context=context)
            
            return Response({'mcqs': questions_dict}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @parser_classes([MultiPartParser, FormParser])
# def image_to_mcqs_view(request):
#     serializer = ImageUploadSerializer(data=request.data)
#     if serializer.is_valid():
#         image = serializer.validated_data['image']
#         context = serializer.validated_data.get('context', '')

#         # Save the uploaded image to a temporary location
#         with tempfile.NamedTemporaryFile(delete=False) as tmp:
#             for chunk in image.chunks():
#                 tmp.write(chunk)
#             tmp_path = tmp.name
        
#         description = image_to_text(tmp_path)
        
#         # Clean up the temporary file
#         os.remove(tmp_path)
        
#         questions_dict = text_to_mcqs(description, context=context)
        
#         return Response({'mcqs': questions_dict}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
