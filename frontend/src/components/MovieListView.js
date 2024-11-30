import React, { useContext } from 'react'
import MovieCard from './micro/MovieCard'
import { MovieContext } from './contexts/MovieContext'

export default function MovieListView() {
  const {movie_list_proxy} = useContext(MovieContext)

  return (
    <div className='listview'>
      {
        movie_list_proxy.map(movie_data => <MovieCard key={movie_data.id} movie_data={movie_data}/>)
      }
    </div>
  )
}
