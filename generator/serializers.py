from rest_framework import serializers

class EducationItem(serializers.Serializer):
    degree = serializers.CharField()
    institution = serializers.CharField()
    location = serializers.CharField()
    date = serializers.CharField()

class ProjectItem(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.CharField()
    problem = serializers.CharField(required=False, allow_blank=True)
    tools = serializers.ListField(child=serializers.CharField(), required=False)
    highlights = serializers.ListField(child=serializers.CharField(), required=False)

class WorkItem(serializers.Serializer):
    role = serializers.CharField()
    org = serializers.CharField()
    date = serializers.CharField()
    bullets = serializers.ListField(child=serializers.CharField(), required=False)

class ResumeRequest(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    education = EducationItem(many=True)
    projects = ProjectItem(many=True, required=False)
    work_history = WorkItem(many=True, required=False)
    skills = serializers.ListField(child=serializers.CharField(), required=False)


