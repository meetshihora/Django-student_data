from django.shortcuts import render
from .models import Student
from django.contrib import messages
# Create your views here.
def index(request):
    students = Student.objects.all()

    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            Student.objects.create(name=name, email=email)
            messages.success(request, 'Student Added Successfully')
        elif 'update' in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')

            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.save()
            messages.success(request, 'Student Updated Successfully')
        elif 'delete' in request.POST:
            id = request.POST.get('id')
            student = Student.objects.get(id=id)
            student.delete()
            messages.success(request, 'Student Deleted Successfully')
    context = {'students': students}
    return render(request, 'index.html', context=context)