from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import *
from .forms import NotesForm
from .models import Notes
from django.urls import reverse

class NotesView(View):
    def get(self, request):
        form = NotesForm()
        note = Notes.objects.all().order_by("-date")
        return render(request, 'app/note.html', {'form': form, 'note': note})

    def post(self, request):
        form = NotesForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return HttpResponseRedirect(reverse('notes:note'))
        else:
            form = NotesForm(request.POST)
            return HttpResponseRedirect(request, 'app/note.html', {'notes': form})  


class DeleteView(View):
    def get(self, request, id):
        form = Notes.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('notes:note'))
        
class EditView(View):
    def get(self, request, id):
        try:
            note = Notes.objects.get(id=id)
        
            form = NotesForm(instance = note)
            return render(request, 'app/edit.html', {'form': form, 'note': note})

        except Notes.DoesNotExist:
            return render(request, 'app/404.html')    

    def post(self, request, id):
        form = NotesForm(request.POST, instance= Notes.objects.get(id=id)) 
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return HttpResponseRedirect(reverse('notes:note'))        