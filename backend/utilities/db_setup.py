import tmdbsimple as tmdb
import os, json, requests, shutil, sys
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.core.files import File

from tmdb_database.models import Movie, Genre

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5
POSTER_ROOT = "https://image.tmdb.org/t/p/w300"
BACKDROP_ROOT_PATH = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
POSTER_CACHE_FOLDER = r"D:\Work\PythonSuli\halado-240907\tmdb_cache\posters"
BACKDROP_CACHE_FOLDER = r"D:\Work\PythonSuli\halado-240907\tmdb_cache\backdrops"
DATABASE_JSON = r"D:\Work\PythonSuli\halado-240907\tmdb_cache\movie_db.json"
PROJECT_ROOT = os.path.dirname(__file__).replace("utilities", "")

def main():
    if not os.path.exists(DATABASE_JSON):
        download_movies()

    reset_django_db()
    run_migrations()
    create_superuser()

    create_genres()
    create_movies()

# Download movie data and media from TMDB
def download_movies():
    if not os.path.exists(os.path.dirname(DATABASE_JSON)):
        os.makedirs(os.path.dirname(DATABASE_JSON))

    movies = tmdb.Movies()
    popular_movies = movies.popular(page=1)["results"]

    movie_list = []
    for movie_data in popular_movies:
        movie_data["poster_path"] = get_image_from_url(f"{POSTER_ROOT}/{movie_data.get('poster_path')}", POSTER_CACHE_FOLDER)
        movie_data["backdrop_path"] = get_image_from_url(f"{BACKDROP_ROOT_PATH}/{movie_data.get('backdrop_path')}", BACKDROP_CACHE_FOLDER)
        movie_list.append(movie_data)

    with open(DATABASE_JSON, "w") as f:
        json.dump(movie_list, f)

def get_image_from_url(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    image_file_name = url.split("/")[-1]
    image_path = os.path.join(folder_path, image_file_name)
    if os.path.exists(image_path):
        return image_path
    
    status = requests.get(url).status_code
    assert status == 200, f"{url} status: {status}"

    img_data = requests.get(url).content
    with open(image_path, "wb") as f:
        f.write(img_data)
    
    print(f"Downloading: {url}")
    return image_path

def reset_django_db():
    # remove db.sqlite3
    db_file = os.path.join(PROJECT_ROOT, "db.sqlite3")
    if os.path.exists(db_file):
        os.remove(db_file)

    tmdb_database_folder = os.path.join(PROJECT_ROOT, "tmdb_database")
    
    # delete __pycache__ folder
    pycache_folder = os.path.join(tmdb_database_folder, "__pycache__")
    if os.path.exists(pycache_folder):
        shutil.rmtree(pycache_folder, ignore_errors=True)
    
    # remove migration files
    migrations_folder = os.path.join(tmdb_database_folder, "migrations")
    for i in os.listdir(migrations_folder):
        if i == "__init__.py":
            continue
        
        if i == "__pycache__":
            continue

        os.remove(os.path.join(migrations_folder, i))
    
    # delete media folder
    media_path = os.path.join(PROJECT_ROOT, "media")
    if os.path.exists(media_path):
        shutil.rmtree(media_path, ignore_errors=True)

def run_migrations():
    # init django project

    # run migrations
    call_command("makemigrations")
    call_command("migrate")

def create_superuser():
    User = get_user_model()
    User.objects.create_superuser("robert", "robert@gmail.com", "testpas123")

def create_genres():
    genre_list = tmdb.Genres().movie_list()["genres"]

    for i in genre_list:
        genre = Genre(name=i["name"], tmdb_id=i["id"])
        genre.save()
        print(f"Genre {i['name']} saved to DB")

def create_movies():
    with open(DATABASE_JSON) as f:
        movie_db = json.load(f)
    
    for movie_data in movie_db:
        movie = Movie()
        movie.tmdb_id = movie_data.get("id", 0)
        movie.title = movie_data.get("title")
        movie.release_date = movie_data.get("release_date")
        movie.vote_average = movie_data.get("vote_average")
        movie.popularity = movie_data.get("popularity")
        movie.overview = movie_data.get("overview")
        movie.language = movie_data.get("original_language")       
        
        # Upload poster and backdrop images
        poster_local_path = movie_data.get("poster_path")
        image_name = os.path.basename(poster_local_path)
        movie.poster_path.save(image_name, File(open(poster_local_path, "rb")))

        backdrop_local_path = movie_data.get("backdrop_path")
        backdrop_name = os.path.basename(backdrop_local_path)
        movie.backdrop_path.save(backdrop_name, File(open(backdrop_local_path, "rb")))

        # set movie genres
        for genre_id in movie_data.get("genre_ids"):
            genre = Genre.objects.get(tmdb_id=genre_id)
            movie.genres.add(genre)

        movie.save()
        print(f"Movie {movie.title} saved to DB")

if __name__ == '__main__':
    create_movies()