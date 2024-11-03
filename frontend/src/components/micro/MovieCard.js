import React from 'react'
import Poster from "../../images/poster.jpg"
import PopularityProgress from "./PopularityProgress"
import { Link } from 'react-router-dom'

export default function MovieCard() {
  return (
    <Link to="/movies/12345-the-wild-robot" className='card movie-card'>
        <div className='poster-container'>
            <img src={Poster} alt="" />
            <PopularityProgress/>
        </div>
        
        <div className='title-container'>
            <h4>The Wild Robot</h4>
            <small>Sep 12, 2024</small>
        </div>
    </Link>
  )
}
