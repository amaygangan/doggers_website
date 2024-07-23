from django.contrib import admin
from blogapp1.models import Doginfo 

# Register your models here.

# admin.site.register(Doginfo)

class DoginfoAdmin(admin.ModelAdmin):
    list_display=["id","breed_name","gender","age","vaccine","price"]
    list_filter=["gender","vaccine"]

admin.site.register(Doginfo,DoginfoAdmin)

admin.site.site_header="Dognation Dashboard"
admin.site.site_title="Dognation Admin"
admin.site.index_title="Dognation Administration"