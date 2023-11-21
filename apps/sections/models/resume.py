from django import forms
from django.db import models

from ..constants import SkillChoices, LevelChoices, EducationChoices, EducationStatusChoices, CategorySkillChoices

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class ResumeBaseModel(BaseModel):
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

    name = models.CharField(max_length=200)


class Task(BaseModel):
    description = models.TextField()
    lang = models.ManyToManyField("Language", through="TaskLang", blank=True)

    def __str__(self):
        return self.description  # What you want to show


class Skill(ResumeBaseModel):
    type = models.IntegerField(choices = SkillChoices.choices, default=SkillChoices.APTITUDES)
    category = models.IntegerField(choices = CategorySkillChoices.choices, default=CategorySkillChoices.PROGRAMING_LANG)
    institute = models.CharField(max_length=200, blank=True)
    level = models.IntegerField(choices = LevelChoices.choices, default=LevelChoices.MEDIUM)


class Experience(BaseModel):
    title = models.CharField(max_length=200) 
    summary = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=200)
    url_company = models.URLField(blank=True)
    logo = models.ImageField(upload_to='images/', blank=True)
    task = models.ManyToManyField(Task, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    lang = models.ManyToManyField("Language", through="ExperienceLang", blank=True)


class Education(BaseModel):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.IntegerField(choices = EducationChoices.choices, default=EducationChoices.UNIVERSITY)
    institute = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(choices = EducationStatusChoices.choices, default=EducationStatusChoices.COMPLETED)
    is_certification = models.BooleanField(default=False)
    lang = models.ManyToManyField("Language", through="EducationLang", blank=True)


class Project(ResumeBaseModel):
    summary = models.TextField(blank=True)
    url = models.URLField(blank=True)


class Contact(ResumeBaseModel):
    """
        Aca van
        linkedin
        git
        fiverr etc
    """
    contact = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=200, blank=True)


class Post(ResumeBaseModel):
    summary = models.TextField()
    description = models.TextField(blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    like = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    view = models.IntegerField(default=0)


class Person(BaseModel):
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    summary = models.TextField()
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    nacionality = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/', blank=True)
    social_contact = models.ManyToManyField(Contact, blank=True)
    experience = models.ManyToManyField(Experience, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    project = models.ManyToManyField(Project, blank=True)
    post = models.ManyToManyField(Post, blank=True)


class Resume(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    lang = models.ManyToManyField("Language", blank=True)
