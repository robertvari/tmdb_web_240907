import React from 'react'
import Poster from "../../images/poster.jpg"
import PopularityProgress from "./PopularityProgress"
import { Link } from 'react-router-dom'

export default function MovieCard({movie_data}) {
  return (
    <Link to="/movies/12345-the-wild-robot" className='card movie-card'>
        <div className='poster-container'>
            <img src={movie_data.poster} alt="" />
            <PopularityProgress/>
        </div>
        
        <div className='title-container'>
            <h4>{movie_data.title}</h4>
            <small>{movie_data.date}</small>
        </div>
    </Link>
  )
}
