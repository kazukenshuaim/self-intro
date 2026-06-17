from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Intro
from django.urls import reverse_lazy
from .forms import IntroForm


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


class IntroCreateView(LoginRequiredMixin, CreateView):
    model = Intro
    form_class = IntroForm
    template_name = 'intros/intro_form.html'
    success_url = reverse_lazy('intros:intro_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': '名前を入力してください。'})
        form.fields['birthday'].widget.attrs.update({'type': 'date', 'class': 'form-control'})
        form.fields['hobby'].widget.attrs.update({'rows': 4, 'class': 'form-control', 'placeholder': '趣味や特技などを自由に記入してください。'})
        return form
    
class IntroUpdateView(LoginRequiredMixin, UpdateView):
    model = Intro
    form_class = IntroForm
    template_name = 'intros/intro_form.html'

    def get_success_url(self):
        return reverse_lazy('intros:intro_detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return Intro.objects.filter(created_by=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': '名前を入力してください。'})
        form.fields['birthday'].widget.attrs.update({'type': 'date', 'class': 'form-control'})
        form.fields['hobby'].widget.attrs.update({'rows': 4, 'class': 'form-control', 'placeholder': '趣味や特技などを自由に記入してください。'})
        return form
    
class IntroDeleteView(LoginRequiredMixin, DeleteView):
    model = Intro
    template_name = 'intros/intro_confirm_delete.html'
    success_url = reverse_lazy('intros:intro_list')

    def get_queryset(self):
        return Intro.objects.filter(created_by=self.request.user)