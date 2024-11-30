import React from 'react'
import Poster from "../../images/poster.jpg"
import PopularityProgress from "./PopularityProgress"
import { Link } from 'react-router-dom'

const API_URL = process.env.REACT_APP_API_URL

export default function MovieCard({movie_data}) {
  return (
    <Link to={`/movies/${movie_data.slug}`} className='card movie-card'>
        <div className='poster-container'>
            <img src={`${API_URL}/${movie_data.poster_path}`} alt="" />
            <PopularityProgress vote_average={movie_data.vote_average}/>
        </div>
        
        <div className='title-container'>
            <h4>{movie_data.title}</h4>
            <small>{movie_data.release_date}</small>
        </div>
    </Link>
  )
}
