import React from 'react'

export default function Footer() {
  return (
    <div className='footer'>
      <div>
        <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg" alt="" />
        <br />
        <button className='inverted-button'>JOIN THE COMMUNITY</button>
      </div>

      <div>
        <h3>THE BASICS</h3>
        <div>About TMDB</div>
        <div>Contact Us</div>
        <div>Support Forums</div>
        <div>API</div>
        <div>System Status</div>
      </div>

      <div>
        <h3>GET INVOLVED</h3>
        <div>Contribution Bible</div>
        <div>Add New Movie</div>
        <div>Add New TV Show</div>
      </div>

      <div>
        <h3>COMMUNITY</h3>
        <div>Guidelines</div>
        <div>Discussions</div>
        <div>Leaderboard</div>
      </div>

      <div>
        <h3>LEGAL</h3>
        <div>Terms of Use</div>
        <div>API Terms of Use</div>
        <div>Privacy Policy</div>
        <div>DMCA Policy</div>
      </div>
    
    </div>
  )
}
