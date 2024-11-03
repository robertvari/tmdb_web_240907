import React, { useState, useEffect } from 'react'
import MovieCard from './micro/MovieCard'
import axios from 'axios'

export default function MovieListView() {
  const [movies, set_movies] = useState([])

  useEffect(() => {
    axios({
      method: "get",
      url: "http://localhost:3001/movies"
    }).then(res => set_movies(res.data))
  }, [])

  return (
    <div className='listview'>
      {
        movies.map(movie_data => <MovieCard movie_data={movie_data}/>)
      }
    </div>
  )
}
