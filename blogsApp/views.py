from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


# This tells what HTTP Methods the client can use within the function below
@api_view(['GET'])
def index(request):
    return Response({"Success": "The setup was successful"})


# This tells what HTTP Methods the client can use within the function below
@api_view(['GET'])
def getAllPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, 200)


@api_view(['GET', 'POST'])
def createPost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The post was successfully created"}, 201)
    else:
        return Response(serializer.errors, 400)


@api_view(['DELETE'])
def deletePost(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response({"Success": "The post was successfully deleted"}, 200)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, 404)


@api_view(['GET'])
def getPost(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data, 200)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, 404)


@api_view(['PATCH'])
def updatePost(request, id):

    title = request.data.get('title')
    content = request.data.get('content')

    try:
        post = Post.objects.get(id=id)

        # Check if request.data is empty
        if not bool(request.data):
            return Response({"error": "Request data is empty"}, status=400)

        # Get all field names from request.data
        field_names = request.data.keys()

        # Check if any field has an empty or None value
        empty_fields = [
            field for field in field_names if not request.data[field]]
        if empty_fields:
            return Response({"error": f"Fields cannot be empty or None: {', '.join(empty_fields)}"}, 400)

        post.title = title
        post.content = content

        post.save()
        return Response({"Success": "The post was successfully updated"}, 200)
    except Post.DoesNotExist:
        return Response({"error": "The post does not exist"}, 400)
