from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.TouristDestinationListAPIView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', views.TouristDestinationDetailAPIView.as_view(), name='destination-detail'),
    path('destinations/create/', views.TouristDestinationCreateAPIView.as_view(), name='destination-create'),
    path('destinations/<int:pk>/delete/', views.TouristDestinationDeleteAPIView.as_view(), name='destination-delete'),
    path('destinations/<int:pk>/update/', views.TouristDestinationUpdateAPIView.as_view(), name='destination-update'),
]

