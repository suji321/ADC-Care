import React from 'react'
import FeatureBox from './FeatureBox'
import featureimage from '../images/feature_1.png'
import featureimage1 from '../images/feature_2.png'
import featureimage2 from '../images/feature_3.png'

const content  = [
  {
    title: "Title 1",
    image: featureimage,
  },
  {
    title: "Title 2",
    image: featureimage1,
  },
  {
    title: "Title 3",
    image: featureimage2,
  }
]

function Feature() {
  return (
    <div id='features'>
        <div className='a-container'>

          {
            content?.map((doc, id) => 
            <FeatureBox image={doc?.image} title={doc?.title} key={id}  />
            )
          }

        </div>
    </div>
  )
}

export default Feature