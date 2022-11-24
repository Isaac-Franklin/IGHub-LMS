from django.db import models
from embed_video.fields import EmbedVideoField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


# Create your models here.

MY_CHOICES = ((1, 'Digital Marketers'),
              (2, 'Full Stack Web Developers'),
              (3, 'Embedded Systems Engineers'),
              (4, 'Product/Graphics Designers'),
              (5, 'Data Scientists'))


class Video_upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Select_Track = models.CharField(max_length=100, null=True, blank=True)
    Select_Title = models.CharField(max_length=25)
    Video_Description = models.TextField(max_length=100, null=True, blank=True)
    Video = EmbedVideoField()  # same like models.URLField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.Video_Title


class Rooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)
    question = models.TextField(max_length=400)
    tips = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.question


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    track = models.CharField(max_length=255, null=True)
    short_description = models.TextField(max_length=300, null=True, blank=True)
    detailed_description = models.TextField(
        max_length=30000, null=True, blank=True)
    resources = models.TextField(max_length=1000, null=True, blank=True)
    mode_of_submission = models.CharField(
        max_length=200, null=True, blank=True)
    task_point = models.IntegerField()
    data_of_submission = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Assignment_submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.SET_NULL, null=True)
    submission = models.CharField(max_length=3000)
    # grade = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.submission[0:50]


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    addressto = models.CharField(max_length=200, null=True, blank=True)
    report = models.TextField(max_length=2000)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.report[0:50]



class GradeStudent(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    assignment = models.CharField(max_length=200, null=True, blank=True)
    submission = models.CharField(max_length=200, null=True, blank=True)
    time_of_submission = models.CharField(max_length=200, null=True, blank=True)
    score = models.CharField(max_length=200, null=True, blank=True)
    feedback = models.CharField(max_length=200, null=True, blank=True)
    # time_of_submission = models.TimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.feedback[0:50]

