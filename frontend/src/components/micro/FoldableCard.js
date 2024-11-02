import React, {useState} from 'react'

export default function FoldableCard({title, content}) {
    const [opened, set_opened] = useState(false)

    return (
        <div className='card sidebar-card' onClick={e => set_opened(!opened)}>
            <div className='header'>
                <b>{title}</b>
                {
                    opened? <i class="fa fa-chevron-down"/> : <i class="fa fa-chevron-right"/>
                }
            </div>
            
            <div>
                {
                    opened? content : null
                }
            </div>
        </div>
    )
}