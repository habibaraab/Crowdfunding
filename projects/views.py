# projects/views.py

from django.contrib import messages
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404


# projects/views.py

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # --- تعديل بسيط هنا ---
            user = form.save() # نحفظ المستخدم ونستقبله في متغير
            # حفظ رقم الهاتف في الـ profile المرتبط بالمستخدم
            user.profile.mobile_phone = form.cleaned_data.get('mobile_phone')
            user.profile.save()
            # ---------------------
            
            messages.success(request, f'تم إنشاء حسابك بنجاح! يمكنك الآن تسجيل الدخول.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'projects/register.html', {'form': form})

# projects/views.py

from django.shortcuts import render, redirect
# ... (باقي أكواد الـ import)

# ... (دالة الـ register)

def home(request):
    return render(request, 'projects/home.html')


# projects/views.py

from django.contrib.auth.decorators import login_required # لاستيراد خاصية التحقق من تسجيل الدخول
from .forms import CustomUserCreationForm, ProjectForm
from .models import Project
# ... (أكواد الـ import الأخرى)

# ... (دوال register و home)

@login_required # <-- هذا السطر يمنع أي شخص غير مسجل من الوصول لهذه الصفحة
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # لا تقم بالحفظ مباشرة، نحتاج لربط المشروع بالمستخدم أولاً
            project = form.save(commit=False)
            project.creator = request.user # تعيين المستخدم الحالي كصاحب المشروع
            project.save()
            return redirect('project_list') # توجيه المستخدم لصفحة كل المشاريع بعد النجاح
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


# projects/views.py

# projects/views.py

def project_list(request):
    projects = Project.objects.all()
    
    search_date = request.GET.get('search_date')
    
    if search_date:
        # الشرط: عرض المشاريع التي بدأت قبل أو في هذا اليوم، وتنتهي بعد أو في هذا اليوم
        projects = projects.filter(start_time__lte=search_date, end_time__gte=search_date)
        
    context = {
        'projects': projects,
        'search_date': search_date,
    }
    return render(request, 'projects/project_list.html', context)

# ... (باقي أكواد import)

# ... (باقي الدوال)

# projects/views.py
from .forms import CustomUserCreationForm, ProjectForm, DonationForm # <-- أضف DonationForm هنا

# ... (باقي الـ imports)

# لا تنس إضافة هذا الديكوريتور
@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    donation_form = DonationForm()

    if request.method == 'POST':
        # هذا الجزء مخصص لمعالجة التبرع فقط
        # (يجب أن يكون لديك name="donate_form" في زر الإرسال بالنموذج)
        if 'donate_form' in request.POST:
            form = DonationForm(request.POST)
            if form.is_valid():
                donation = form.save(commit=False)
                donation.donator = request.user
                donation.project = project
                donation.save()
                messages.success(request, 'شكراً لك! تم تسجيل تبرعك بنجاح.')
                return redirect('project_detail', project_id=project.id)

    context = {
        'project': project,
        'donation_form': donation_form
    }
    return render(request, 'projects/project_detail.html', context)

# projects/views.py

from django.http import HttpResponseForbidden
# ... (imports)

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    # تحقق مما إذا كان المستخدم الحالي هو صاحب المشروع
    if project.creator != request.user:
        return HttpResponseForbidden("ليس لديك الصلاحية لتعديل هذا المشروع.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project) # عرض النموذج مملوءاً بالبيانات الحالية
    
    return render(request, 'projects/project_form.html', {'form': form, 'form_type': 'تعديل'})


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.creator != request.user:
        return HttpResponseForbidden("ليس لديك الصلاحية لحذف هذا المشروع.")

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
        
    return render(request, 'projects/project_confirm_delete.html', {'project': project})