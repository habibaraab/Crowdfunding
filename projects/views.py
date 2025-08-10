# projects/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, ProjectForm, DonationForm
from .models import Project

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.mobile_phone = form.cleaned_data.get('mobile_phone')
            user.profile.save()
            
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'projects/register.html', {'form': form})

def home(request):
    featured_projects = Project.objects.order_by('-id')[:3]
    context = {
        'featured_projects': featured_projects
    }
    return render(request, 'projects/home.html', context)

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    
    search_date = request.GET.get('search_date')
    
    if search_date:
        projects = projects.filter(start_time__lte=search_date, end_time__gte=search_date)
        
    context = {
        'projects': projects,
        'search_date': search_date,
    }
    return render(request, 'projects/project_list.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    donation_form = DonationForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
            
        if 'donate_form' in request.POST:
            form = DonationForm(request.POST)
            if form.is_valid():
                donation = form.save(commit=False)
                donation.donator = request.user
                donation.project = project
                donation.save()
                messages.success(request, 'Thank you! Your donation has been recorded successfully.')
                return redirect('project_detail', project_id=project.id)

    context = {
        'project': project,
        'donation_form': donation_form
    }
    return render(request, 'projects/project_detail.html', context)

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.creator != request.user:
        return HttpResponseForbidden("You do not have permission to edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_form.html', {'form': form, 'form_type': 'Edit'})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.creator != request.user:
        return HttpResponseForbidden("You do not have permission to delete this project.")

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
        
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

def logout_view(request):
    logout(request)
    return redirect('home')