from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Message, Notification, MessageCategory, Comment, Tag, Link

def index(request):
    return render(request, 'polls/index.html')

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.message = Message.objects.get(pk=self.kwargs['message_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('message_detail', kwargs={'pk': self.kwargs['message_id']})

