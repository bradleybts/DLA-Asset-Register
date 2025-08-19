from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    access_level = models.ForeignKey('UserClass', on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

class Asset(models.Model):
    STATUS_CHOICES = [
        ('in_use', 'In Use'),
        ('in_storage', 'In Storage'),
        ('under_repair', 'Under Repair'),
        ('disposed', 'Disposed'),
    ]

    asset_name = models.CharField(max_length=255)
    asset_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    warranty_expiration = models.DateField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_storage')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assets')
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    previous_service_date = models.DateField(null=True, blank=True)
    upcoming_service_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.asset_name

class ServiceHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='service_history')
    previous_service_date = models.DateField()
    upcoming_service_date = models.DateField(null=True, blank=True)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    technician = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.service_type} for {self.asset.asset_name} on {self.previous_service_date}"

class TechnicalIssue(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='technical_issues')
    date = models.DateField()
    issue = models.TextField()
    resolution = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Issue for {self.asset.asset_name} on {self.date}"

class DisposalInfo(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE, related_name='disposal_info')
    disposal_date = models.DateField()
    disposal_method = models.CharField(max_length=100)
    reason = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Disposal of {self.asset.asset_name} on {self.disposal_date}"

class UserClass(models.Model):
    name = models.CharField(max_length=50, unique=True) # Admin, IT Staff, Basic User

    def __str__(self):
        return self.name

class Rights(models.Model):
    user_class = models.OneToOneField(UserClass, on_delete=models.CASCADE, related_name='rights')
    can_view_admin = models.BooleanField(default=False)
    can_view_assets = models.BooleanField(default=False)
    can_view_asset_overview = models.BooleanField(default=False)
    can_view_user_management = models.BooleanField(default=False)
    can_view_reports = models.BooleanField(default=False)

    def __str__(self):
        return f"Rights for {self.user_class.name}"
