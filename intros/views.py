from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Intro


class IntroListView(LoginRequiredMixin, ListView):
    model = Intro
    template_name = 'intros/intro_list.html'
    context_object_name = 'intros'

    def get_queryset(self):
        return Intro.objects.filter(created_by=self.request.user)


class IntroDetailView(LoginRequiredMixin, DetailView):
    model = Intro
    template_name = 'intros/intro_detail.html'
    context_object_name = 'intro'

    def get_queryset(self):
        return Intro.objects.filter(created_by=self.request.user)