import React from 'react'
import SearchBox from './micro/SearchBox'

export default function Navbar() {
  return (
    <div className='navbar'>
      <div style={{display:"inherit"}}>
        <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" alt="" />

        <div className='nav-item'>Movies</div>
        <div className='nav-item'>TV Shows</div>
        <div className='nav-item'>People</div>
        <div className='nav-item'>More</div>
      </div>

      <div style={{display:"inherit"}}>
        <div className='nav-item'>Login</div>
        <div className='nav-item'>Join TMDB</div>
        <SearchBox/>
      </div>
    </div>
  )
}
