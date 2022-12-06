from rest_framework import serializers
from .models import (
    Quiz,
    Question,
    Option,
)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
        model = Question
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
        model = Option
        exclude = ('is_correct','question')
