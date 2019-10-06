import React, { Component } from 'react';

import { Link } from 'react-router-dom';

import Navbar from 'react-bootstrap/Navbar'

class Header extends Component {
  render() {
    return (
      <header>
          <Link to="/">Home</Link> | <Link to="/RoverView">RoverView</Link> | <Link to="/ArmView">ArmView</Link>
      </header>
    );
  }
}

export default Header;