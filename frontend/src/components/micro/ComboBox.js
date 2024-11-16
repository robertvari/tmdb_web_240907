import React, {useEffect, useState} from 'react'

export default function ComboBox({items, selected_item}) {
    const [opened, set_opened] = useState(false)
    const [current_item, set_current_item] = useState("")

    function handle_item_clicked(item_name){
        set_current_item(item_name)
        set_opened(false)
    }

    useEffect(() => {
        set_current_item(selected_item)
    }, [selected_item])
    
    return (
        <div className='combo-box'>
            <div className='combo-button' onClick={e => set_opened(!opened)}>
                {current_item} {opened? <i className="fa fa-chevron-down"/> : <i className="fa fa-chevron-left"/>}
            </div>

            {
                opened?
                    <div className='combo-items-container'>
                        {
                            items.map(menu_item => <div key={menu_item} className={`combo-item ${current_item === menu_item? "active": ""}`} onClick={e => handle_item_clicked(menu_item)}>{menu_item}</div>)
                        }
                    </div>
                :
                    null
            }
        </div>
    )
}