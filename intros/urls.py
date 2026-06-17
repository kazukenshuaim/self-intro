from django.urls import path
from .views import (
    IntroListView, IntroDetailView,
    IntroCreateView, IntroUpdateView, IntroDeleteView
)

app_name = 'intros'

urlpatterns = [
    path('', IntroListView.as_view(), name='intro_list'),
    path('<int:pk>/', IntroDetailView.as_view(), name='intro_detail'),
    path('create/', IntroCreateView.as_view(), name='intro_create'),
    path('<int:pk>/update/', IntroUpdateView.as_view(), name='intro_update'),
    path('<int:pk>/delete/', IntroDeleteView.as_view(), name='intro_delete'),
]
