from django.contrib import admin
from instructorApp.models import User,Category,Course,Module,Lesson,Order
# Register your models here.

admin.site.register(User)
admin.site.register(Category)

class CourseModel(admin.ModelAdmin):
    exclude=['owner']
admin.site.register(Course,CourseModel)

def save_model(self,request,obj,form,change):
    if not change:
        obj.owner=request.user
        super().save_model(request,obj,form,change)


class ModuleModel(admin.ModelAdmin):
    exclude=['order']
admin.site.register(Module,ModuleModel)
                           
class LessonModel(admin.ModelAdmin):
    exclude=['order']
admin.site.register(Lesson,LessonModel)  
admin.site.register(Order)

