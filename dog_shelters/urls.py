from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in_status', views.index, name='status'),
    path('token_details', views.token_details, name='token_details'),
    path('', views.shelter_list, name='shelter_list'),
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),
    path('dog/register', views.DogCreateView.as_view(), name='dog_register'),
]
