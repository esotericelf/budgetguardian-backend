from django.urls import path
from .user_views import get_user_data
from .category_views import get_category_sums
from .date_range_views import get_category_sums_by_date_range
from .token_views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Budget Guardian!")

urlpatterns = [
    path('', home, name='home'),  # Root URL pattern
    path('user-data/<str:uid>/', get_user_data, name='get_user_data'),  # Include uid parameter
    path('category-sums/<str:uid>/', get_category_sums, name='get_category_sums'),  # Include uid parameter
    path('category-sums-by-date/<str:uid>/', get_category_sums_by_date_range, name='get_category_sums_by_date_range'),  # Include uid parameter
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Use custom token view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]