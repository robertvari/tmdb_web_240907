import React, {createContext, useState, useEffect} from "react"
import axios from "axios"

const API_URL = process.env.REACT_APP_API_URL

export const MovieContext = createContext(true)


export const MovieProvider = (props) => {
    const [genre_list, set_genre_list] = useState([])
    const [movie_list, set_movie_list] = useState([])
    const [movie_list_proxy, set_movie_list_proxy] = useState([])
    const [search, set_search] = useState("")
    const [genre, set_genre] = useState("")
    const [sorting, set_sorting] = useState("Popularity Descending")
    const [sort_query, set_sort_query] = useState("-popularity")

    const sort_list = [
        "Popularity Descending",
        "Popularity Ascending",
        "Rating Descending",
        "Rating Ascending",
        "Release Date Descending",
        "Release Date Ascending",
        "A-Z Descending",
        "A-Z Ascending"
    ]

    const fetch_genre_list = () => {
        axios({
            method: "get",
            url: `${API_URL}/api/tmdb/genres/`
        }).then(response => set_genre_list(response.data))
    }

    const fetch_movie_list = () => {
        axios({
            method: "get",
            url: `${API_URL}/api/tmdb/movies/?sorting=${sort_query}`
        }).then(res => {set_movie_list(res.data); set_movie_list_proxy(res.data)})
    }

    // fetch genre and movie list from server
    useEffect(() => {
        fetch_genre_list()
        fetch_movie_list()
    }, [])

    //Filter proxy movie list
    useEffect(() => {
        // create a local copy of the movie_list
        let _movie_list = [...movie_list]
        
        // filter movies by title
        if(search.length > 0){
            _movie_list = _movie_list.filter(movie_data => movie_data.title.toLowerCase().includes(search.toLowerCase()))
        }

        // filter movies by genre
        if(genre.length > 0){
            _movie_list = _movie_list.filter(movie_data => movie_data.genres.includes(genre))
        }

        set_movie_list_proxy(_movie_list)
    }, [search, genre])

    // Trigger for handling sort changes
    useEffect(() =>{
        const sort_mapping = {
            "Popularity Descending" : "-popularity",
            "Popularity Ascending" : "popularity",
            "Rating Descending" : "-vote_average",
            "Rating Ascending" : "vote_average",
            "Release Date Descending" : "-release_date",
            "Release Date Ascending" : "release_date",
            "A-Z Descending" : "title",
            "A-Z Ascending" : "-title"
        }

        set_sort_query(sort_mapping[sorting])
    }, [sorting])

    useEffect(() => {
        fetch_movie_list()
    }, [sort_query])

    return(
        <MovieContext.Provider value={{
            sort_list: sort_list,
            genre_list: genre_list,
            movie_list: movie_list,
            movie_list_proxy: movie_list_proxy,
            search: search,
            set_search: set_search,
            genre: genre,
            set_genre: set_genre,
            sorting: sorting,
            set_sorting: set_sorting
        }}>

            {props.children}

        </MovieContext.Provider>
    )
}