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
        sorting = request.GET.get("sorting")
        movie_data = self.get_movies(sorting)
        return Response(movie_data)
    
    def get_movies(self, sorting):
        movies = []

        for movie in Movie.objects.order_by(sorting):
            movies.append(
                {
                    "title": movie.title,
                    "poster_path": movie.poster_path.url,
                    "vote_average": int(round(movie.vote_average)*10),
                    "popilarity": movie.popularity,
                    "release_date": movie.release_date,
                    "genres": [genre.name for genre in movie.genres.all()],
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

class MovieDetalsView(APIView):
    def get(self, request, slug):
        movie = Movie.objects.get(slug=slug)
        movie_details = {
            "id": movie.id,
            "tmdb_id": movie.tmdb_id,
            "title": movie.title,
            "genres": [i.name for i in movie.genres.all()],
            "release_date": movie.release_date,
            "poster_path": movie.poster_path.url,
            "backdrop_path": movie.backdrop_path.url,
            "vote_average": int(round(movie.vote_average)*10),
            "popularity": movie.popularity,
            "overview": movie.overview,
            "language": movie.language
        }
        return Response(movie_details)