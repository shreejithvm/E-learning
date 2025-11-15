from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from instructorApp.forms import InstructorCreateForm
from instructorApp.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

class InstructorView(View):
    def get(self,request):
        form=InstructorCreateForm()
        return render(request,'instructor_register.html',{'form':form})
    def post(self,request):
        form_instance=InstructorCreateForm(request.POST)
        print(form_instance)
        if form_instance.is_valid():
            res=form_instance.save(commit=False)
            res.is_superuser=True
            res.role="instructor"
            res.is_staff=True
            res.password=make_password(form_instance.cleaned_data.get("password"))
            form_instance.save()
            return HttpResponse("data added")



