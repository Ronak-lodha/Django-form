from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_success')  # 👈 redirect to success view
    else:
        form = StudentForm()
    
    return render(request, 'students/add_student.html', {'form': form})

# ✅ Success page view
def student_success(request):
    return render(request, 'students/success.html')

def student_list(request):
    students = Student.objects.all()  # sab student record
    return render(request, 'students/student_list.html', {'students': students})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # success ke baad list page
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')
