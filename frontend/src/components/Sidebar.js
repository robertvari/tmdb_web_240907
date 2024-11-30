import React, {useState, useEffect, useContext} from 'react'
import FoldableCard from './micro/FoldableCard'
import ComboBox from './micro/ComboBox'
import { MovieContext } from './contexts/MovieContext'


function Sorting(){
  const {sorting_list} = useContext(MovieContext)
  const [default_item, set_default_item] = useState("")


  // Waits for sorting_list and sets default_item state
  useEffect(() => {
    if(sorting_list.length > 0){
      set_default_item(sorting_list[0])
    }
  }, [sorting_list])

  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      <p>Sort Results by</p>
      <ComboBox items={sorting_list} selected_item={default_item}/>
    </div>
  )
}

function Filters(){
  const {genre_list} = useContext(MovieContext)

  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      {
        genre_list.map(genre_item => <div key={genre_item.id}>{genre_item.name}</div>)
      }
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
