from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render


@api_view(['GET'])
def top_authors_and_works_rest(request):
    """
    Top 10 authors and there 10 best works.
    """
    if request.method == "GET":
        authors = Author.objects.all().order_by('-total_books_sold')[:5]
        serializer= AuthorSerializer(authors, many=True)
        return Response(serializer.data, template_name="rest_framework/api.html")



def top_authors_and_works(request):
    """
    Top 10 authors and there 10 best works.
    """
    if request.method == "GET":
        authors = Author.objects.all().order_by('-total_books_sold')[:5]
        serializer= AuthorSerializer(authors, many=True)
        return render(request,"bookstore/top_authors_and_their_works.html",{"serializer":serializer.data})
