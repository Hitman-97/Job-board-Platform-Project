from django.contrib import admin
from .models import JobListing, CandidateProfile, JobApplication

admin.site.register(JobListing)
admin.site.register(CandidateProfile)
admin.site.register(JobApplication)
