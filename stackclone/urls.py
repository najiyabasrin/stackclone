"""stackclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stack import views
from django.conf import settings
from django.conf.urls.static import static

from stackapi.views import Questionsview,Answerview,QuestionDeleteView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/question",Questionsview,basename="questions")
router.register("api/answer",Answerview,basename="answer")



urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignupView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path("questions/<int:id>/answer/add",views.add_answer,name="add-answer"),
    path("answers/<int:id>/upvote",views.upvote_view,name="upvote"),
    path("signout",views.sign_out,name="signout"),
    path("questions/all",views.MyQuestionsView.as_view(),name="my-questions"),
    path("jwt/token/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("questions/<int:pk>",QuestionDeleteView.as_view())
]+router.urls
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
