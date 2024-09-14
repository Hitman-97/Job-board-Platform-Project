from django.db import models
from django.contrib.auth.models import User

# Job Listing Model
class JobListing(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Candidate Profile Model
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Job Application Model
class JobApplication(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    candidate_profile = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.candidate_profile.user.username} applied for {self.job_listing.title}'
