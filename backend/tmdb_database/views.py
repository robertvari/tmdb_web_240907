from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MovieListView(APIView):
    def get(self, request):
        movie_data = []
        return Response(movie_data)
    
class NavbarView(APIView):
    def get(self, request):
        nav_item_list = [
            "Movies",
            "TV Shows",
            "People",
            "More"
        ]
        return Response(nav_item_list)
    
class SortListView(APIView):
    def get(self, request):
        sort_list = [
            "Popularity Descending",
            "Popularity Ascending",
            "Rating Descending",
            "Rating Ascending",
            "Release Date Descending",
            "Release Date Ascending",
            "A-Z Descending",
            "A-Z Ascending"
        ]
        return Response(sort_list)

class GenreListView(APIView):
    # Retrieve data
    def get(self, request):
        genre_list = [
            "Action",
            "Adventure",
            "Animation",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Family",
            "Fantasy"
        ]
        return Response(genre_list)
    
    # # Create data
    # def post(self, request):
    #     return Response("Post request")
    
    # # Delete data
    # def delete(self, request):
    #     return Response("Delete request")
    
    # # Update data
    # def patch(self, request):
    #     return Response("Update request")

    # CRUD = Create, Retrieve, Update, Delete