from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, CompanyViewSet, WatchlistView, AddToWatchlistView, RemoveFromWatchlistView, ItemList, ItemDetail

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('watchlist/', WatchlistView.as_view(), name='watchlist-list'),
    path('watchlist/add/', AddToWatchlistView.as_view(), name='watchlist-add'),
    path('watchlist/remove/', RemoveFromWatchlistView.as_view(), name='watchlist-remove'),
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]