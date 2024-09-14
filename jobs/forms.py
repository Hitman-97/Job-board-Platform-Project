from django import forms
from .models import JobListing, CandidateProfile, JobApplication

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'company', 'location', 'description']

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['resume', 'bio']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
