# projects/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from .models import validate_egyptian_phone_number # نستدعي دالة التحقق من المودل

from .models import validate_egyptian_phone_number # تأكد من وجود هذا السطر

# ... (باقي الـ imports)

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='مطلوب.')
    last_name = forms.CharField(max_length=30, required=True, help_text='مطلوب.')
    email = forms.EmailField(max_length=254, required=True, help_text='مطلوب. البريد الإلكتروني يجب أن يكون فريداً.')
    # --- أضف هذا الحقل ---
    mobile_phone = forms.CharField(label="رقم الهاتف", validators=[validate_egyptian_phone_number], required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile_phone')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_time', 'end_time', 'main_picture']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'مثال: إطلاق تطبيق تعليمي للأطفال'}),
            'details': forms.Textarea(attrs={'placeholder': 'اشرح كل تفاصيل مشروعك هنا...'}),
            'total_target': forms.NumberInput(attrs={'placeholder': 'مثال: 250000'}),
            'start_time': forms.DateInput(attrs={'type': 'date'}),
            'end_time': forms.DateInput(attrs={'type': 'date'}),
        }


# projects/forms.py
# ... (imports)
from .models import Donation

# ... (باقي كلاسات الـ Forms)

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'أدخل مبلغ التبرع', 'class': 'donation-input'}),
        }
        labels = {
            'amount': 'المبلغ (بالجنيه المصري)'
        }