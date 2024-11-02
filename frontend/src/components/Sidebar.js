import React from 'react'
import FoldableCard from './micro/FoldableCard'

export default function Sidebar() {
  return (
    <div className='sidebar'>
      <h2>Popular Movies</h2>
      <FoldableCard title="Sort" content="Sort functions"/>
      <FoldableCard title="Where to watch" content="Channel icons"/>
      <FoldableCard title="Filters" content="Filter functions..."/>
    </div>
  )
}
