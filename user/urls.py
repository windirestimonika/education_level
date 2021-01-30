from django.urls import path
from .views import user_list, user_detail, UserAPIView, UserDetails

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('detail/<int:pk>', UserDetails.as_view())
]