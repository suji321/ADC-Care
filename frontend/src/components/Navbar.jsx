import { Button, Checkbox, Input, Modal, Row, Text } from '@nextui-org/react'
import React, { useState } from 'react'
import logo from '../images/adc-home.png'

function Navbar() {
    const [nav,setnav] = useState(false);
    const [modalVisible, setModalVisible] =  useState(false)

    const changeBackground = () => {
        if (window.scrollY >= 50) {
            setnav(true)
        }
        else{
            setnav(false)
        }
    }
    window.addEventListener('scroll', changeBackground)
  return (
    <div>
        <nav className={nav ? 'nav active' : 'nav'}>
            <a href='#' className='logo'> 
              <img src={logo} alt=''/> 
            </a>
            <input type='checkbox' className='menu-btn' id='menu-btn' />
            <label className='menu-icon' for='menu-btn'>
                <span className='nav-icon'></span>    
            </label>
            <ul className='menu'>
                <li><a href='#'>Home</a></li>
                <li><a href='#'>About Us</a></li>
                <li><a href='#'>Services</a></li>
                <li><a href='#'>Our Doctors</a></li>
                <li><a href='#'>Gallery</a></li>
                <li><a href='#'>Testimonial</a></li>
                <li><a href='#' className='active  ' onClick={() => setModalVisible(true)}>Login</a></li>
            </ul>
        </nav>
        <Modal
        closeButton
        aria-labelledby="modal-title"
        open={modalVisible}
        onClose={() => setModalVisible(!modalVisible)}
    >
        <Modal.Header>
            <Text id="modal-title" size={18}>
            Welcome to {''}
            <Text b size={18}>
                ADC 
            </Text>
            </Text>
        </Modal.Header>
        <Modal.Body>
            <Input
                clearable
                bordered
                fullWidth
                color="primary"
                size="lg"
                placeholder="Email"
                // contentLeft={<Mail />}
            />
            <Input
                clearable
                bordered
                fullWidth
                color="primary"
                size="lg"
                placeholder="Password"
                // contentLeft={<Password />}
            />
            <Row justify="space-between">
            <Checkbox>
                <Text size={14}>
                Remember me
                </Text>
            </Checkbox>
            <Text size={14}>
                Forgot password?
            </Text>
            </Row>
        </Modal.Body>
        <Modal.Footer>
            <Button auto flat color="error" onClick={() => setModalVisible(false)}>
            Close
            </Button>
            <Button auto onClick={() => setModalVisible(false)}>
            Sign in
            </Button>
        </Modal.Footer>
    </Modal>
    </div>
  )
}

export default Navbar