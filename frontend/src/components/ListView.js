import React from 'react'
import Sidebar from "./Sidebar"
import MovieListView from "./MovieListView"

export default function ListView() {
  return (
    <div className='content horizontal-box'>
      <Sidebar/>
      <MovieListView/>
    </div>
  )
}
