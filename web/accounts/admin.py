from django.contrib import admin
from accounts.models import User, Candidate, Employer, Language

# Register your models here.
admin.site.register(User)
admin.site.register(Candidate)
admin.site.register(Employer)
admin.site.register(Language)