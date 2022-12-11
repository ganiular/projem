from django.db import models
from django.dispatch import receiver
import os

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=25, unique=True)
    project_detail = models.CharField(max_length=150)
    project_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.project_name

@receiver(models.signals.post_delete, sender=Project)
def delete_Project_images(sender, instance, **kwargs):
    # Deletes Image Renditions
    instance.project_image.delete_all_created_images()
    # Deletes Original Image
    instance.project_image.delete(save=False)


class Student(models.Model):
    student_name = models.CharField(max_length=50, unique=False)
    student_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student_deadline = models.DateField()

    def __str__(self):
        return self.student_name



class Member(models.Model):
    name = models.CharField(max_length=25)
    reg = models.CharField(max_length=20)

    def __str__(self):
        return self.name
