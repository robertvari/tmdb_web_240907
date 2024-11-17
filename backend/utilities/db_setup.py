import tmdbsimple as tmdb
import os, json, requests

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5
POSTER_TOOT = "https://image.tmdb.org/t/p/w300"
BACKDROP_ROOT_PATH = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
POSTER_CACHE_FOLDER = ""
BACKDROP_CACHE_FOLDER = ""
DATABASE_JSON = ""

# Download movie data and media from TMDB
def download_movies():
    pass

# Create a clean Django migration
# Register superuser
# Add genres
# Add Sort items
# Add Movies