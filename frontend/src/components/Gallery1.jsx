import React from 'react'
import { Carousel } from 'react-responsive-carousel'
import featureimage from '../images/feature_1.png'
import featureimage1 from '../images/feature_2.png'
import featureimage2 from '../images/feature_3.png'

function Gallery1() {
  return (
    <Carousel>
        <div>
            <img src={featureimage} alt="" />
        </div>
        <div>
            <img src={featureimage1} alt="" />
        </div>
        <div>
            <img src={featureimage2} alt="" />
        </div>
    </Carousel>
  )
}

export default Gallery1