import React from 'react'
import {useParams} from "react-router-dom"
import Poster from "../images/poster.jpg"
import Backdrop from "../images/backdrop.webp"
import PopularityProgress from "../components/micro/PopularityProgress"

export default function MovieDetails() {
    const {slug} = useParams()

    return (
        <div>
            <div className='movie-details-header'>
                <img src={Backdrop} alt="" className='backdrop'/>

                <div className='content movie-details-container'>
                    <img src={Poster} alt="" className='poster'/>
                    <div>
                        <h1>The Wild Robot (2024)</h1>
                        <p>09/27/2024 (US) Animation, Science Fiction, Family 1h 42m</p>
                        <PopularityProgress/>

                        <h3>Overview</h3>
                        <p>After a shipwreck, an intelligent robot called Roz is stranded on an uninhabited island. To survive the harsh environment, Roz bonds with the island's animals and cares for an orphaned baby goose.</p>
                    </div>
                </div>
            </div>
        </div>
    )
}
