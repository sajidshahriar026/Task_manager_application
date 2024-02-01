from django.contrib import admin

from .models import Task, Image

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3



class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'due_date', 'priority', 'completed']


    def get_queryset(self, request):
        queryset = super(TaskAdmin, self).get_queryset(request)
        return queryset.order_by('priority')


    inlines = [ImageInline]




admin.site.register(Task, TaskAdmin)
admin.site.register(Image)
