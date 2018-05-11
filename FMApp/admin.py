from django.contrib import admin
from FMApp.models import (Company, CompanyProfile,
                          Facility, FacilityManager,
                          Request, Apartment, Tenant)

# Register your models here.


class RequestAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        user = request.user
        company = user.profile.company
        if user.is_superuser:
            comp_requests = Request.objects.all()
        else:
            comp_requests = Request.objects.filter(facilitator=company)
        return comp_requests


admin.site.register(Company)
admin.site.register(CompanyProfile)
admin.site.register(Facility)
admin.site.register(FacilityManager)
admin.site.register(Apartment)
admin.site.register(Tenant)
admin.site.register(Request)
