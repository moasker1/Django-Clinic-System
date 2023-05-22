from django.contrib import admin
from .models import طفل



class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'الاسم', 'تاريح_الحجز')
    search_fields = ['الاسم', 'تاريح_الحجز', 'id']
    list_filter = ['الاسم', 'تاريح_الحجز', 'id','الحالة']

    
admin.site.register(طفل, ChildAdmin)

admin.site.site_header = 'المـــركز التخصصي لرعاية الأطفال'
admin.site.site_title = "العيــادة"
admin.site.index_title =  'د. حمدي زغلول'