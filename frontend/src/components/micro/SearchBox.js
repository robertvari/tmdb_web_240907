import React, {useContext, useState} from 'react'
import { MovieContext } from '../contexts/MovieContext'

export default function SearchBox() {
    const {search, set_search} = useContext(MovieContext)
    const [opened, set_opened] = useState(false)

    return (
        <div onClick={e => set_opened(!opened)} className='search-box-container'>
            {
                opened?
                <input type="text" placeholder='Search...' value={search} onChange={e => set_search(e.target.value)} onClick={e => e.stopPropagation()}/>
                :
                null
            }
            <i className="fa fa-search" aria-hidden="true"/>
        </div>
    )
}
