from django.contrib import admin
from .models import Master,TermsCondition,AboutUs,Companyinfo

# Register your models here.

class MaterialTermsConditionAdmin(admin.ModelAdmin):
    icon_name = 'contact_support'

admin.site.register(Master)
admin.site.register(AboutUs)
admin.site.register(Companyinfo)
admin.site.register(TermsCondition,MaterialTermsConditionAdmin)