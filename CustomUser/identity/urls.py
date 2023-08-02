# Importing Required Librarie
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views


app_name = 'identity'

# Defining Url pattern for Account Creation, delete, Login and Change password(While Login)
urlpatterns = [
    path('user/register', views.UserListView.as_view(), name='userregister'),
    path('user/login', views.UserloginViewset.as_view(), name='userlogin'),
    path('user/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('user/token/refresh',
         jwt_views.TokenRefreshView.as_view(), name='access-token'),
    path('user/retrieve/<int:pk>',
         views.User_ModelRetrieveAPIView.as_view(), name='userlogin'),
    path('user/update/<int:pk>',
         views.UpdateUserViewset.as_view(), name='userupdate'),
    path('user/nupdate/<int:pk>',
         views.UpdateUserNormalViewset.as_view(), name='userupdate'),
    path('user/change-password/',
         views.ChangePasswordView.as_view(), name='change-password'),
    path('user/teacher/list', views.TeacherListView.as_view(), name='teacher-list'),
    path('cred', views.get_credentials, name='google'),

    # search name api
    path('search/name', views.GetUserFullnameAPIView.as_view()),


    # admin is_approve
    path('user/list', views.Adminis_approveListView.as_view()),
    # admin update approve
    path('user/approve/<int:pk>', views.AdminUpdateApproveViewset.as_view()),

    # user forget password
    path('user/forget-password/', views.UserForgetPasswordView.as_view()),

    # user forget password
    path('user/otp-varification/', views.VarifyOTPView.as_view()),


    # user email sending
    path('send-email/', views.EmailView.as_view()),
]
