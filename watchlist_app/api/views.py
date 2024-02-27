from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from .serializers import MovieSerializer

@api_view(['GET','POST'])
def movie_list(request):

    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True) 

        return Response(serializer.data)
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):

    if request.method=='GET':
        try:
            movies=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)

        serializer=MovieSerializer(movies) 
        return Response(serializer.data)
    if request.method=='PT':
        movies=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

