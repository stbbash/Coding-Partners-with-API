from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from website.models import Member
from .serializers import MemberSerializer


@api_view(['GET'])
def getRoutes(request, format=None):
    routes = [
        'GET /api',
        'GET /api/mymembers',
        'GET /api/mymember/:id'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getMembers(request, format=None):
    if request.method == 'GET':
        mymembers = Member.objects.all()
        serializer = MemberSerializer(mymembers, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def getMember(request, pk, format=None):
    try:
        mymember = Member.objects.get(id=pk)
    except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        serializer = MemberSerializer(mymember, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MemberSerializer(mymember, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        mymember.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        