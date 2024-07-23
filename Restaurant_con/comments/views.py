from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import CommentForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class CommentView(LoginRequiredMixin,SuccessMessageMixin,FormView):
    template_name = 'comments.html'
    form_class=CommentForm
    success_url = reverse_lazy('comments')
    success_message = "Yorumunuzu Aldık! Teşekkür Ederiz!!"
    login_url='login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.name = f"{self.request.user.first_name} {self.request.user.last_name}"
        form.instance.email = self.request.user.email
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


    
