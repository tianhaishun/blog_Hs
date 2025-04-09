from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.school} - {self.degree}"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Skills'),
        ('soft', 'Soft Skills'),
        ('tools', 'Tools & Technologies'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    proficiency = models.IntegerField(default=3)  # 1-5 scale

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.company} - {self.position}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    responsibilities = models.TextField()
    achievements = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    status = models.CharField(max_length=200)
    summary = models.TextField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.name 