"""
URL configuration for budgetify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# budgetify/urls.py
from django.urls import path
from .views import get_user_data, get_category_sums, get_category_sums_by_date_range
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Budget Guardian!")

urlpatterns = [
    path('', home, name='home'),  # Root URL pattern
    path('user-data/', get_user_data, name='get_user_data'),
    path('category-sums/', get_category_sums, name='get_category_sums'),
    path('category-sums-by-date/', get_category_sums_by_date_range, name='get_category_sums_by_date_range'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]