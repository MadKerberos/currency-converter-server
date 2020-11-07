from django.urls import path
from . import views
from api.views.auth.login import Login
from api.views.auth.logout import Logout
from api.views.auth.signup import Signup
from api.views.personalInfo import PersonalInfoView,PersonalInfoModifyView
from api.views.test_auth import WelcomeAuth
from api.views.authentication import logout
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('', views.index, name='index'),
    #path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    #path('login/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('login/', Login.as_view(), name='api_token_auth'),  # <-- And here
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', Signup.as_view(), name="signup"),
    path('welcomeAuth/', WelcomeAuth.as_view()),


    path('personalInfo/<int:id>/', PersonalInfoView.as_view()),
    path('personalInfo/', PersonalInfoView.as_view()),
    path('personalInfo/modify/', PersonalInfoModifyView.as_view())
]