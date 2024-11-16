from rest_framework.views import APIView
from rest_framework.response import Response
import tmdbsimple as tmdb
from datetime import datetime
tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5

POSTER_TOOT = "https://image.tmdb.org/t/p/w300"


# Create your views here.
class MovieListView(APIView):
    def get(self, request):
        movie_data = self.get_movies()
        return Response(movie_data)
    
    def get_movies(self):
        movies = tmdb.Movies()
        popular_movies = movies.popular(page=1).get("results")
        
        movie_data_model = []
        for i in popular_movies:
            movie_data_model.append({
                "id": i.get("id"),
                "title": i.get("title"),
                "date": datetime.strptime(i.get("release_date"), "%Y-%m-%d").strftime("%Y %B %d"),
                "poster": f"{POSTER_TOOT}{i.get('poster_path')}",
                "vote_average": int(round(i.get("vote_average") * 10))
            })

        return movie_data_model
    
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