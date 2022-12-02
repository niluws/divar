from django.urls import path
from. import views
app_name='account'
urlpatterns=[
    path('phone',views.ValidatePhoneNumber.as_view(),name='get_phone'),
    path('register',views.UserRegisterView.as_view(),name='register'),
     path('exist_user',views.ValidateExistUser.as_view(),name='validate_exist_user' )

]

