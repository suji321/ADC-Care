import React from 'react'
import { Parallax } from 'react-scroll-parallax'
import Navbar from './Navbar'

function Header() {
  return (
    <div id='main'>
        <Navbar/>
        <div className='name'>
            <h1><span>Lorem ipsom</span><br/>
            With confidence and creativity</h1>
            <p className='details'>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
            <a href='#' className='cv-btn'></a>
        </div>
    </div>
  )
}

export default Header