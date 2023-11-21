from django.db import models

from .resume import BaseModel, ResumeBaseModel, Task, Education, Experience


class Language(ResumeBaseModel):
    code = models.CharField(blank=False, max_length=50)
    status = models.ForeignKey("LanguageStatus", on_delete=models.DO_NOTHING, default=1)
    encoding = models.CharField(blank=True, max_length=50)


class ResumeBaseRelationsLangModel(BaseModel):
    class Meta:
        abstract = True

    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    translation = models.CharField(max_length=150)


class TaskLang(ResumeBaseRelationsLangModel):
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)


class EducationLang(ResumeBaseRelationsLangModel):
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200) 
    summary = models.TextField(blank=True) 


class ExperienceLang(ResumeBaseRelationsLangModel):
    education = models.ForeignKey(Experience, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200) 
    summary = models.TextField(blank=True)


class LanguageStatus(ResumeBaseModel):
    class Meta:
        verbose_name = "language status"
        verbose_name_plural = "Language status"
    lang = models.ManyToManyField(Language, through="LanguageStatusLang", blank=True)


class LanguageStatusLang(ResumeBaseRelationsLangModel):
    language_status = models.ForeignKey(LanguageStatus, on_delete=models.DO_NOTHING)
    