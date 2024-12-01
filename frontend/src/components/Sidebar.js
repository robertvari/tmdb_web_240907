import React, {useState, useEffect, useContext} from 'react'
import FoldableCard from './micro/FoldableCard'
import ComboBox from './micro/ComboBox'
import { MovieContext } from './contexts/MovieContext'


function Sorting(){
  const {sort_list, sorting, set_sorting} = useContext(MovieContext)

  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      <p>Sort Results by</p>
      <ComboBox items={sort_list} selected_item={sorting} on_changed={set_sorting}/>
    </div>
  )
}

function Filters(){
  const {genre_list, genre, set_genre} = useContext(MovieContext)

  const handle_genre_clicked = (genre_name) => {
    if(genre === genre_name){
      set_genre("")
    }else{
      set_genre(genre_name)
    }
  }

  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      {
        genre_list.map(genre_item => 
        <div className={genre_item.name === genre? 'active':''} key={genre_item.id} onClick={e => handle_genre_clicked(genre_item.name)}>{genre_item.name}</div>
      )}
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
