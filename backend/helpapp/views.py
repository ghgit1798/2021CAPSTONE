from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_list(request):
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_detail(request, user_number):
    user = User.objects.filter(user_number=user_number)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def study_list(request):
    study_list = Study.objects.all()
    serializer = StudySerializer(study_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def study_detail(request, study_id):
    study = Study.objects.filter(study_id=study_id)
    serializer = StudySerializer(study, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_study(request):
    if request.method == 'POST':
        user_id = request.GET.get('user_id')
        study_name = request.GET.get('study_name')
        study_exp = request.GET.get('study_exp')
        study = Study(study_name=study_name, user_id=user_id, study_exp=study_exp)
        study.save()
        user_study = User_Study(user_id=user_id, study_id=study.study_id)
        user_study.save()
        serializer = StudySerializer(study)

        return JsonResponse(serializer.data, status=400)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def study_userlist(request, study_id):
    userlist = User_Study.objects.filter(study_id=study_id)
    serializer = UserStudySerializer(userlist, many=True)
    return JsonResponse(serializer.data, status=200)

@csrf_exempt
def test(request):
    # 프론트는 Json 형식의 데이터를 받아서 화면에 표시
    if request.method == 'GET':
        return JsonResponse({
            'message': 'GET 테스트'
        }, json_dumps_params={'ensure_ascii': False}, status=200)
    elif request.method == 'POST':
        return JsonResponse({
            'message': 'POST 테스트'
        }, json_dumps_params={'ensure_ascii': False}, status=200)




