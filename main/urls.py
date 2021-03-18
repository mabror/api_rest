from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', views.Index.as_view()),
    path('post/', views.PostList.as_view()),
    path('detail/<int:pk>/', views.PostDetail.as_view()),
]