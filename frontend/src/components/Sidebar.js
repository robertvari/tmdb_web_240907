import React, {useState, useEffect} from 'react'
import FoldableCard from './micro/FoldableCard'
import ComboBox from './micro/ComboBox'
import axios from 'axios'

function Sorting(){
  const [sorting_list, set_sorting_list] = useState([])
  const [default_item, set_default_item] = useState("")

  // Gets the sort list fron Django server
  useEffect(() => {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/sort-list/"
    }).then(response => set_sorting_list(response.data))
  }, [])


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
  const [filters, set_filters] = useState([])

  useEffect(() => {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/genre-list/"
    }).then(response => set_filters(response.data))
  }, [])

  return(
    <div className='card-content' onClick={e => e.stopPropagation()}>
      {
        filters.map(genre_item => <div key={genre_item}>{genre_item}</div>)
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
