from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title


class Resident(models.Model):
    resident_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.resident_id

    def get_absolute_url(self):

        return reverse("resident_detail", kwargs={"pk": self.pk})


class BarangayOfficials(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    official_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.full_name


class Requests(models.Model):
    request = models.CharField(max_length=50, unique=True)
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.request} - {self.status}"


class Announcements(models.Model):
    announcement = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_by = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class EmergencyHotlines(models.Model):
    hotline_id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    barangay_official = models.ForeignKey(BarangayOfficials, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.agency_name
