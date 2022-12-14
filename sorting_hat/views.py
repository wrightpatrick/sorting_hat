from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def student_list(request):
    students = models.Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list.html', context)

def student_detail(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    context = {'student': student}
    return render(request, 'student_detail.html', context)

class StudentDetailView(generic.DetailView):
    model = models.Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class StudentCreateView(generic.CreateView):
    model = models.Student
    template_name = 'student_form.html'
    fields = ['first_name', 'last_name']

class StudentUpdateView(generic.CreateView):
    model = models.Student
    template_name = 'student_form.html'
    fields = ['first_name', 'last_name']

class StudentDelete(generic.DeleteView):
    model = models.Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
