from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IntroListView(LoginRequiredMixin, TemplateView):
    template_name = 'intros/intro_list.html'