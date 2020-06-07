from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students

# Create your views here.
def student_list(request):
    context={'student_list':Students.objects.all()}
    return render(request,"student_register/student_list.html",context)

def student_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form= StudentForm()
        else:
             students=Students.objects.get(pk=id)
             form=StudentForm(instance=students)
        return render(request,"student_register/student_form.html",{'form':form})
    else:
        if id==0:
            form = StudentForm(request.POST)
        else:
            students = Students.objects.get(pk=id)
            form=StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
        return redirect('/student/list')

def student_delete(request,id):
    students = Students.objects.get(pk=id)
    students.delete()
    return redirect('/student/list')