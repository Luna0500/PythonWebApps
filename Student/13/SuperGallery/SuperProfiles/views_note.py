from pathlib import Path
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .views_functions import IsNoteCreatorMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from .models import Note
from .views_reporter import get_reporter
    
class NoteListView(ListView):
    template_name = 'note/list.html'
    model = Note
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Note.objects.all()
        }

class NoteDetailView(DetailView):
    template_name = 'note/detail.html'
    model = Note
    context_object_name = 'note'

class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = "note/add.html"
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.reporter = get_reporter(self.request.user)
        return super().form_valid(form)
    

class NoteUpdateView(IsNoteCreatorMixin, UpdateView):
    template_name = "note/edit.html"
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(IsNoteCreatorMixin, DeleteView):
    template_name = 'note/delete.html'
    model = Note
    success_url = reverse_lazy('note_list')