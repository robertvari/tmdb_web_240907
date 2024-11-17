import tmdbsimple as tmdb
import os, json, requests, shutil

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5
POSTER_ROOT = "https://image.tmdb.org/t/p/w300"
BACKDROP_ROOT_PATH = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
POSTER_CACHE_FOLDER = r"D:\Work\PythonSuli\halado-240907\tmdb_cache\posters"
BACKDROP_CACHE_FOLDER = r"D:\Work\PythonSuli\halado-240907\tmdb_cache\backdrops"
DATABASE_JSON = r"D:\Work\PythonSuli\halado-240907\tmdb_cache\movie_db.json"
PROJECT_ROOT = os.path.dirname(__file__).replace("utilities", "")

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

def main():
    if not os.path.exists(DATABASE_JSON):
        download_movies()

    reset_django_db()

def reset_django_db():
    db_file = os.path.join(PROJECT_ROOT, "db.sqlite3")
    if os.path.exists(db_file):
        os.remove(db_file)

    tmdb_database_folder = os.path.join(PROJECT_ROOT, "tmdb_database")
    
    # delete __pycache__ folder
    pycache_folder = os.path.join(tmdb_database_folder, "__pycache__")
    if os.path.exists(pycache_folder):
        shutil.rmtree(pycache_folder, ignore_errors=True)
    
    migrations_folder = os.path.join(tmdb_database_folder, "migrations")
    for i in os.listdir(migrations_folder):
        if i == "__init__.py":
            continue
        os.remove(os.path.join(migrations_folder, i))


main()