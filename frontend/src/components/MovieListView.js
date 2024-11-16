import React, { useState, useEffect } from 'react'
import MovieCard from './micro/MovieCard'
import axios from 'axios'

export default function MovieListView() {
  const [movies, set_movies] = useState([])

  useEffect(() => {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/movies/"
    }).then(res => set_movies(res.data))
  }, [])

  return (
    <div className='listview'>
      {
        movies.map(movie_data => <MovieCard key={movie_data.id} movie_data={movie_data}/>)
      }
    </div>
  )
}
