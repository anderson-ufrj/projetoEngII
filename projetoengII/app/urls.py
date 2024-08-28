from django.urls import path
from .views import LoginView, LogoutView, IndexView, SubmitOrderView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('submit_order/', SubmitOrderView.as_view(), name='submit_order'),
]
