import React, {useState} from 'react'

export default function SearchBox() {
    const [opened, set_opened] = useState(false)

    return (
        <div onClick={e => set_opened(!opened)} className='search-box-container'>
            {
                opened?
                <input type="text" placeholder='Search...' onClick={e => e.stopPropagation()}/>
                :
                null
            }
            <i className="fa fa-search" aria-hidden="true"/>
        </div>
    )
}
