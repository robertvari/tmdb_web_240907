import React from 'react'

export default function PopularityProgress({vote_average}) {
  return (
    <div className='popularity-progress-container'>
        <p>{vote_average}<span>%</span></p>
    </div>
  )
}
