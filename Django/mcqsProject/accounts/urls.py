# from django.urls import path
# from .views import RegisterTeacherView, RegisterStudentView, LoginView

# urlpatterns = [
#     path('register/teacher/', RegisterTeacherView.as_view(), name='register-teacher'),
#     path('register/student/', RegisterStudentView.as_view(), name='register-student'),
#     path('login/', LoginView.as_view(), name='login'),
# ]


from django.urls import path
from . import views
from .views import ImageToMCQsView


urlpatterns = [
    path('login/', views.login, name='login'),
    path('users/', views.create_school_user, name='create_school_user'),
    path('images/', views.create_image, name='create_image'),
    path('images/all/', views.get_all_images, name='get_all_images'),
    path('teachers/all/', views.get_all_teachers, name='get_all_teachers'),
    path('quizzes/', views.create_quiz, name='create_quiz'),
    path('quizzes/<int:image_id>/', views.get_quizzes_by_image, name='get_quizzes_by_image'),
    path('images/<int:teacher_id>/', views.get_images_by_teacher, name='get_images_by_teacher'),
    path('generate-mcqs/', ImageToMCQsView.as_view(), name='generate-mcqs'),
    # path('api/image-to-mcqs/', image_to_mcqs_view, name='image_to_mcqs'),


]
