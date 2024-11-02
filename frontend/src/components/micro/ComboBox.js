import React, {useState} from 'react'

export default function ComboBox({items, selected_item}) {
    const [opened, set_opened] = useState(false)
    const [current_item, set_current_item] = useState(selected_item)

    function handle_item_clicked(item_name){
        set_current_item(item_name)
        set_opened(false)
    }
    
    return (
        <div className='combo-box'>
            <div className='combo-button' onClick={e => set_opened(!opened)}>
                {current_item} {opened? <i class="fa fa-chevron-down"/> : <i class="fa fa-chevron-left"/>}
            </div>

            {
                opened?
                    <div className='combo-items-container'>
                        {
                            items.map(menu_item => <div className={`combo-item ${current_item === menu_item? "active": ""}`} onClick={e => handle_item_clicked(menu_item)}>{menu_item}</div>)
                        }
                    </div>
                :
                    null
            }
        </div>
    )
}