from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['name']) < 5:
            errors['name'] = "Course name should be longer than 5 characters"

        if len(postData['description']) < 15:
            errors['description'] = "Course description should be longer than 15 characters"

        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Description(models.Model):
    description = models.TextField()
    course = models.OneToOneField(Course, on_delete = models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.TextField() 
    course = models.ForeignKey(Course, related_name = "comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
