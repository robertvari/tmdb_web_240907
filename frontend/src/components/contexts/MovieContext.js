import React, {createContext, useState, useEffect} from "react"
import axios from "axios"

const API_URL = process.env.REACT_APP_API_URL

export const MovieContext = createContext(true)


export const MovieProvider = (props) => {
    const [sorting_list, set_sorting_list] = useState([])
    const [genre_list, set_genre_list] = useState([])
    const [movie_list, set_movie_list] = useState([])
    const [movie_list_proxy, set_movie_list_proxy] = useState([])
    const [search, set_search] = useState("")

    const fetch_sorting_list = () => {
        axios({
            method: "get",
            url: `${API_URL}/api/tmdb/sort-list/`
        }).then(response => set_sorting_list(response.data))
    }

    const fetch_genre_list = () => {
        axios({
            method: "get",
            url: `${API_URL}/api/tmdb/genres/`
        }).then(response => set_genre_list(response.data))
    }

    const fetch_movie_list = () => {
        axios({
            method: "get",
            url: `${API_URL}/api/tmdb/movies/`
        }).then(res => {set_movie_list(res.data); set_movie_list_proxy(res.data)})
    }

    // fetch sorting list
    useEffect(() => {
        fetch_genre_list()
        fetch_sorting_list()
        fetch_movie_list()
    }, [])

    useEffect(() => {
        let _movie_list = [...movie_list]
        if(search.length > 0){
            _movie_list = _movie_list.filter(movie_data => movie_data.title.toLowerCase().includes(search.toLowerCase()))
        }
        set_movie_list_proxy(_movie_list)
    }, [search])

    return(
        <MovieContext.Provider value={{
            sorting_list: sorting_list,
            genre_list: genre_list,
            movie_list: movie_list,
            movie_list_proxy: movie_list_proxy,
            search: search,
            set_search: set_search
        }}>

            {props.children}

        </MovieContext.Provider>
    )
}