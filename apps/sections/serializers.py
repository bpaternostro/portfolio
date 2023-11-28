from itertools import groupby
from django.conf import settings
from rest_framework import serializers
from .models.resume import Person, Experience, Education, Skill, Project, Contact, Task, Post, Message
from .constants import SkillChoices, InteractFieldsChoices

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["description"]


class EducationSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='get_status_display')
    type_name = serializers.CharField(source='get_type_display')

    class Meta:
        model = Education
        fields = ["id","title", "summary", "start_date", "end_date", "type_name", "institute", "status_name", "is_certification"]


class SkillSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='get_category_display')
    type_name = serializers.CharField(source='get_type_display')

    class Meta:
        model = Skill
        fields = ["id","name", "type_name", "category_name", "institute", "level"]


class ExperienceSerializer(serializers.ModelSerializer):
    task = serializers.SerializerMethodField()
    skill = SkillSerializer(many=True)
    class Meta:
        model = Experience
        fields = ["id", "title", "start_date", "end_date", "company", "url_company", "task", "skill", "logo"]
    
    def get_task(self, obj):
        return [t.description for t in obj.task.all()]

    def to_representation(self, instance):
        response = super(ExperienceSerializer, self).to_representation(instance)
        if instance.logo:
            response['logo'] = settings.MEDIA_ROOT + instance.logo.name
        return response

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ["id", "created_on", "updated_on", "name", "summary", "description", "link", "image", "like", "share", "skill", "view"]

    def get_skill(self, obj):
        return [s.name for s in obj.skill.all()]
    
    def to_representation(self, instance):
        response = super(PostSerializer, self).to_representation(instance)
        if instance.image:
            response['image'] = settings.MEDIA_ROOT + instance.image.name
        return response


class PostInteractSerializer(serializers.ModelSerializer):
    field = serializers.ChoiceField(choices = InteractFieldsChoices)
    class Meta:
        model = Post
        fields = ["field"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField()
    education = EducationSerializer(many=True)
    aptitude = serializers.SerializerMethodField()
    certification = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    soft_skill = serializers.SerializerMethodField()
    project = ProjectSerializer(many=True)
    post = serializers.SerializerMethodField()
    social_contact = ContactSerializer(many=True)

    class Meta:
        model = Person
        fields = ["first_name","last_name","summary","nacionality","address","picture","experience", "education", "aptitude", "certification", "language", "soft_skill", "project", "post", "social_contact"]
        depth = 1

    def get_certification(self, obj):
        skills = SkillSerializer(obj.skill.exclude(institute="").exclude(type=SkillChoices.LANGUAGE).exclude(type=SkillChoices.SOFT_SKILLS), many=True).data
        sorted_list = sorted(skills, key=lambda x: x["institute"])
        return {key: list(group) for key, group in groupby(sorted_list, key=lambda x: x["institute"])} 

    def get_aptitude(self, obj):
        skills = SkillSerializer(obj.skill.filter(type=SkillChoices.APTITUDES, institute=""), many=True).data
        sorted_list = sorted(skills, key=lambda x: x["category_name"])
        return {key: list(group) for key, group in groupby(sorted_list, key=lambda x: x["category_name"])} 
    
    def get_language(self, obj):
        skills = SkillSerializer(obj.skill.filter(type=SkillChoices.LANGUAGE), many=True).data
        sorted_list = sorted(skills, key=lambda x: x["category_name"])
        return {key: list(group) for key, group in groupby(sorted_list, key=lambda x: x["category_name"])} 
    
    def get_soft_skill(self, obj):
        skills = SkillSerializer(obj.skill.filter(type=SkillChoices.SOFT_SKILLS), many=True).data
        sorted_list = sorted(skills, key=lambda x: x["category_name"])
        return {key: list(group) for key, group in groupby(sorted_list, key=lambda x: x["category_name"])} 
    
    def get_post(self, obj):
        posts = obj.post.all().order_by('-created_on')
        return PostSerializer(posts, many=True).data
    
    def get_experience(self, obj):
        experiences = obj.experience.all().order_by('-end_date')
        return ExperienceSerializer(experiences, many=True).data

    def to_representation(self, instance):
        response = super(PersonSerializer, self).to_representation(instance)
        if instance.picture:
            response['picture'] = settings.MEDIA_ROOT + instance.picture.name
        return response