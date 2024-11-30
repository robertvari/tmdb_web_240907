from rest_framework.views import APIView
from rest_framework.response import Response
import tmdbsimple as tmdb
from datetime import datetime

from tmdb_database.models import Genre, Movie

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5

POSTER_TOOT = "https://image.tmdb.org/t/p/w300"


# Create your views here.
class MovieListView(APIView):
    def get(self, request):
        movie_data = self.get_movies()
        return Response(movie_data)
    
    def get_movies(self):
        movies = []

        for movie in Movie.objects.all():
            movies.append(
                {
                    "title": movie.title,
                    "poster_path": movie.poster_path.url,
                    "vote_average": movie.vote_average,
                    "release_date": movie.release_date,
                    "genres": [{"id": genre.id, "name": genre.name} for genre in movie.genres.all()],
                    "slug": movie.slug
                }
            )
        
        return movies
    
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
        genre_list = self.get_genre_list()
        return Response(genre_list)
    
    def get_genre_list(self):
        genre_list = []

        for genre in Genre.objects.all():
            genre_list.append(
                {"id": genre.id, "tmdb_id": genre.tmdb_id, "name": genre.name}
            )
        return genre_list
    
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