from django.urls import path
from .views import IntroListView, IntroDetailView

app_name = 'intros'

urlpatterns = [
    path('', IntroListView.as_view(), name='intro_list'),
    path('<int:pk>/', IntroDetailView.as_view(), name='intro_detail'),
]
