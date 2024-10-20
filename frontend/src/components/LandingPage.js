import React from 'react'
import Sidebar from "./Sidebar"
import MovieListView from "./MovieListView"

export default function LandingPage() {
  return (
    <div>
      <Sidebar/>
      <MovieListView/>
      <button>Load More</button>
    </div>
  )
}
