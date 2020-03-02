from django.urls import path
#from . import views
from .views import SignUpView, ChangePasswordResetDoneSuccessView, ChangePasswordResetDoneView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change_password/', ChangePasswordResetDoneView.as_view(), name='change_password'),
    path('change_password_done', ChangePasswordResetDoneSuccessView.as_view(), name = 'change_password_done'),
]
