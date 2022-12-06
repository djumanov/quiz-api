from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer

from .models import Quiz, Question, Option


class QuizListView(APIView):
    def get(self, request: Request):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)


class QuestionListView(APIView):
    def get(self, request: Request, pk):
        quiz = Quiz.objects.get(id=pk)
        question = Question.objects.filter(quiz=quiz)
        data = []
        for q in question:
            options = Option.objects.filter(question=q)
            # Oprion serializer exclude 'is_correct' field
            option_serializer = OptionSerializer(options, many=True, context={'test': 1}) 
            data.append({
                'question': q.title,
                'id': q.id,
                'options': option_serializer.data,
            })

        return Response(data)


class CheckView(APIView):
    def get(self, request: Request, pk):
        option = Option.objects.get(id=pk)
        return Response({"result": option.is_correct})