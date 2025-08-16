from rest_framework import generics, viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.db.utils import IntegrityError
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth import authenticate
from .models import Company, Watchlist, Item
from .serializers import CompanySerializer, WatchlistSerializer, RegisterSerializer, ItemSerializer
from .filters import CompanyFilter

def index(request):
    return render(request, 'index.html')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED
            )

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CompanyFilter
    search_fields = ['company_name', 'symbol']

class WatchlistView(generics.ListAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Watchlist.objects.filter(user=user).select_related('company')

class AddToWatchlistView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)
        if not isinstance(request.data, dict):
            return Response({'error': 'Invalid request body format.'}, status=status.HTTP_400_BAD_REQUEST)
        ticker = request.data.get('ticker', '').strip()
        
        if not ticker:
            return Response({'error': 'Ticker not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            company = Company.objects.get(symbol=ticker)
            user = request.user
            
            if Watchlist.objects.filter(user=user, company=company).exists():
                return Response({'message': f'Company "{ticker}" is already on your watchlist.'}, status=status.HTTP_200_OK)

            Watchlist.objects.create(user=user, company=company)
            return Response({'message': f'Company "{ticker}" added to watchlist.'}, status=status.HTTP_201_CREATED)
        
        except Company.DoesNotExist:
            return Response({'error': f'Company with ticker "{ticker}" not found.'}, status=status.HTTP_404_NOT_FOUND)
        except MultipleObjectsReturned:
            return Response({'error': 'Duplicate entries found in the database. Please contact support.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except IntegrityError:
            return Response({"error": "Company is already in the watchlist."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return Response({'error': 'An unexpected server error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RemoveFromWatchlistView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        ticker = request.data.get('ticker', None)
        if not ticker:
            return Response({'error': 'Ticker not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            company = Company.objects.get(symbol=ticker)
            
            watchlist_item = Watchlist.objects.get(user=request.user, company=company)
            watchlist_item.delete()
            
            return Response({'message': f'Company "{ticker}" removed from watchlist.'}, status=status.HTTP_200_OK)
        except (Company.DoesNotExist, Watchlist.DoesNotExist):
            return Response({'error': f'Company with ticker "{ticker}" not found in watchlist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)