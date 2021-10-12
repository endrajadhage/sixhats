from six_hats import settings
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import UserDetail
from rest_framework.pagination import PageNumberPagination
# Create your views here.
@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = settings.PAGESIZE
        students = UserDetail.objects.all()
        result_page = paginator.paginate_queryset(students, request)
        serializers = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializers.data)

@api_view(['GET','POST','PUT','DELETE'])
def user_details(request,pk):
    try:
        student = UserDetail.objects.get(pk=pk)
    except UserDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = UserSerializer(student)
        return Response(serializers.data)

    elif (request.method == 'POST'):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializers = UserSerializer(student,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)