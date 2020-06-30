from django.shortcuts import render
from . import StudentForm
# Create your views here.
def index(request):
    return render(request,'form_app/index.html')

def form_name_view(request):
    form=StudentForm()
    return render(request,'form_app/student.html',{'form':form})
