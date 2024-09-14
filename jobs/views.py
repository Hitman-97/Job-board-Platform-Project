from django.shortcuts import render, get_object_or_404, redirect
from .models import JobListing, CandidateProfile, JobApplication
from .forms import JobListingForm, CandidateProfileForm, JobApplicationForm

def job_list(request):
    jobs = JobListing.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

def post_job(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobListingForm()
    return render(request, 'jobs/post_job.html', {'form': form})

def apply_job(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    if request.method == 'POST':
        candidate_profile = CandidateProfile.objects.get(user=request.user)
        application = JobApplication(job_listing=job, candidate_profile=candidate_profile)
        application.save()
        return redirect('job_list')
    return render(request, 'jobs/apply_job.html', {'job': job})

def profile(request):
    if request.method == 'POST':
        form = CandidateProfileForm(request.POST, request.FILES, instance=request.user.candidateprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CandidateProfileForm(instance=request.user.candidateprofile)
    return render(request, 'jobs/profile.html', {'form': form})
