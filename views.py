from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from .forms import SignupForm
from django.contrib.auth import login

@login_required
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
def dashboard(request):

    students = Student.objects.all()

    return render(
        request,
        'dashboard.html',
        {'students':students}
    )


@login_required
def create_student(request):

    form = StudentForm()

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    return render(
        request,
        'student_form.html',
        {'form':form}
    )


@login_required
def update_student(request,pk):

    student = get_object_or_404(
        Student,
        id=pk
    )

    form = StudentForm(
        instance=student
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    return render(
        request,
        'student_form.html',
        {'form':form}
    )


@login_required
def delete_student(request,pk):

    student = get_object_or_404(
        Student,
        id=pk
    )

    if request.method == 'POST':

        student.delete()

        return redirect('dashboard')

    return render(
        request,
        'delete.html',
        {'student':student}
    )
    
# Create your views here.
