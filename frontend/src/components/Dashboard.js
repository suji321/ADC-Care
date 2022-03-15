import React, { Component } from "react";
import Modal from './Modal.js';
import { Button } from "@mui/material";
class Dashboard extends Component {
  // ...
  render() {
    return (
      <main>
        <h1>React Modal</h1>
        <Modal show={this.state.show} handleClose={this.hideModal}>
          <p>Modal</p>
        </Modal>
        <button type="button" onClick={this.showModal}>
          Open
        </button>
        <Button>Hello World</Button>
      </main>
    );
  }
}

export default Dashboard
