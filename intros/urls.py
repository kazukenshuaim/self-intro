from django.urls import path
from .views import IntroListView

app_name = 'intros'

urlpatterns = [
    path('', IntroListView.as_view(), name='intro_list'),
]