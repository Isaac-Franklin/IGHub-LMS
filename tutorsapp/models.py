from django.db import models
from django.contrib.auth.models import User



class Scores(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    track = models.CharField(max_length=200, blank=True, null=True)
    score = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']

    def __str__(self):
        return self.name



class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quiz = models.CharField(max_length=2000, blank=True, null=True)
    prize = models.CharField(max_length=150, blank=True, null=True)
    notes = models.TextField(blank=True, null=True, max_length=2000)
    # expire_at = models.CharField(blank=True, null=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-edited_at', '-created_at']

    def __str__(self):
        return self.quiz


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    response = models.CharField(blank=True, null=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.response

# class CreateAssignment(models.Model):

    