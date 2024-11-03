import React from 'react'
import Sidebar from "./Sidebar"
import MovieListView from "./MovieListView"
import TvShowListView from "./TvShowListView"
import PeopleListView from "./PeopleListView"
import { useLocation } from 'react-router-dom'

export default function ListView() {
  const location = useLocation()

  return (
    <div className='content horizontal-box'>
      {location.pathname !== "/people"? <Sidebar/>: null}
      
      {location.pathname === "/"? <MovieListView/> : null}
      {location.pathname === "/tvshows"? <TvShowListView/> : null}
      {location.pathname === "/people"? <PeopleListView/> : null}
      
    </div>
  )
}
