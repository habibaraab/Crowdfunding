# projects/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# هذه الدالة لا تحتاج أي import من ملفات أخرى في تطبيقك
def validate_egyptian_phone_number(value):
    pattern = r"^(010|011|012|015)\d{8}$"
    if not re.match(pattern, value):
        raise ValidationError("الرجاء إدخال رقم هاتف مصري صحيح (مثال: 01012345678).")


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشروع")
    details = models.TextField(verbose_name="تفاصيل المشروع")
    total_target = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ المستهدف")
    start_time = models.DateField(verbose_name="تاريخ بدء الحملة")
    end_time = models.DateField(verbose_name="تاريخ انتهاء الحملة")
    main_picture = models.ImageField(upload_to='project_pics/', null=True, blank=True, verbose_name="الصورة الرئيسية")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_projects")

    @property
    def current_funding(self):
        # نجمع كل التبرعات المرتبطة بهذا المشروع
        return self.donations.aggregate(total=models.Sum('amount'))['total'] or 0

    @property
    def funding_percentage(self):
        if self.total_target > 0:
            return (self.current_funding / self.total_target) * 100
        return 0

    def __str__(self):
        return self.title


class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مبلغ التبرع")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="donations", verbose_name="المشروع")
    donator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations_made", verbose_name="المتبرع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التبرع")

    def __str__(self):
        return f"{self.amount} EGP for {self.project.title} by {self.donator.username}"
    

# projects/models.py
# ... (imports)
from django.db.models.signals import post_save
from django.dispatch import receiver

# ... (كل الموديلات الأخرى)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_phone = models.CharField(max_length=11, validators=[validate_egyptian_phone_number], verbose_name="رقم الهاتف")

    def __str__(self):
        return f'{self.user.username} Profile'

# --- هذا الجزء يقوم بإنشاء profile تلقائياً مع كل user جديد ---
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# ----------------------------------------------------------------