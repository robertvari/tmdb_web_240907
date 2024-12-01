import React, { useContext, useEffect } from 'react'
import {useParams} from "react-router-dom"
import Poster from "../images/poster.jpg"
import Backdrop from "../images/backdrop.webp"
import PopularityProgress from "../components/micro/PopularityProgress"
import { MovieContext } from './contexts/MovieContext'

const API_URL = process.env.REACT_APP_API_URL

export default function MovieDetails() {
    const {slug} = useParams()
    const {fetch_movie_details, movie_details} = useContext(MovieContext)

    useEffect(() => {
        fetch_movie_details(slug)
    }, [])

    if(!movie_details){
        return null
    }

    return (
        <div>
            <div className='movie-details-header'>
                <img src={`${API_URL}${movie_details.backdrop_path}`} alt="" className='backdrop'/>

                <div className='content movie-details-container'>
                    <img src={`${API_URL}${movie_details.poster_path}`} alt="" className='poster'/>
                    <div>
                        <h1>{movie_details.title}</h1>
                        <p>{movie_details.release_date} ({movie_details.language}) {movie_details.genres.join(", ")}</p>
                        <PopularityProgress vote_average={movie_details.vote_average}/>

                        <h3>Overview</h3>
                        <p>{movie_details.overview}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}
