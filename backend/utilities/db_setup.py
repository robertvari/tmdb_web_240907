import tmdbsimple as tmdb
import os, json, requests

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5
POSTER_ROOT = "https://image.tmdb.org/t/p/w300"
BACKDROP_ROOT_PATH = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
POSTER_CACHE_FOLDER = r"D:\Work\PythonSuli\halado-240907\posters"
BACKDROP_CACHE_FOLDER = r"D:\Work\PythonSuli\halado-240907\backdrops"
DATABASE_JSON = r"D:\Work\PythonSuli\halado-240907\movie_db.json"

# Download movie data and media from TMDB
def download_movies():
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


# Create a clean Django migration
# Register superuser
# Add genres
# Add Sort items
# Add Movies