import React from 'react'
import FoldableCard from './micro/FoldableCard'
import ComboBox from './micro/ComboBox'

function Sorting(){
  const options = [
    "Popularity Descending",
    "Popularity Ascending",
    "Rating Descending",
    "Rating Ascending",
    "Release Date Descending",
    "Release Date Ascending",
    "A-Z Descending",
    "A-Z Ascending"
  ]

  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      <p>Sort Results by</p>
      <ComboBox items={options} selected_item={options[0]}/>
    </div>
  )
}

function Filters(){
  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      Filters...
    </div>
  )
}

export default function Sidebar() {
  return (
    <div className='sidebar'>
      <h2>Popular Movies</h2>
      <FoldableCard title="Sort" content={<Sorting/>}/>
      <FoldableCard title="Filters" content={<Filters/>}/>
    </div>
  )
}
