import React from 'react'
import SearchBox from './micro/SearchBox'
import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <div className='navbar'>
      <div style={{display:"inherit"}}>
        <Link to="/">
          <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" alt="" />
        </Link>

        <Link to="/" className='nav-item'>Movies</Link>
        <Link to="/tvshows" className='nav-item'>TV Shows</Link>
        <Link to="/people" className='nav-item'>People</Link>
        <Link to="/more" className='nav-item'>More</Link>
      </div>

      <div style={{display:"inherit"}}>
        <Link to="/login" className='nav-item'>Login</Link>
        <Link to="/registration" className='nav-item'>Join TMDB</Link>
        <SearchBox/>
      </div>
    </div>
  )
}
