from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TradePortal import views
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='company')

urlpatterns = [
    path('', views.index, name='index'),
    
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('TradePortal.urls')),

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/watchlist/', views.WatchlistView.as_view(), name='watchlist-list'),
    path('api/watchlist/add/', views.AddToWatchlistView.as_view(), name='watchlist-add'),
    path('api/watchlist/remove/', views.RemoveFromWatchlistView.as_view(), name='watchlist-remove'),
]