import React from 'react'
import Header from './components/Header'
import About from './components/About'
import Presentation from './components/Presentation'
import Feature from './components/Feature'
import aboutimage from './images/Frame 19.png'
import aboutimage1 from './images/download.png'
import Contact from './components/Contact'
import Doctors from './components/Doctors'
import Gallery1 from './components/Gallery1'
import Services from './components/Services'

function App() {
  return (
    <div className='App'>
      <Header />
      <About />
      <Services />
      <Doctors/>
      <Contact />
    </div>
  )
}

export default App