from django.db import models

# Create your models here.
class Reminder(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reminders', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    dashboard = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    text = models.CharField(max_length=5000)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
    
class Groop(models.Model):
    owner = models.ForeignKey('auth.User', related_name='groops', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    home = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)
    image = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class Thot(models.Model):
    groop = models.ForeignKey(Groop, related_name='thots', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    text = models.CharField(max_length=5000)
    dashboard = models.BooleanField(default=False)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.text