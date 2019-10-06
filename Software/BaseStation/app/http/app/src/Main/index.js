import React, { Component } from 'react';
import { Switch, Route, } from 'react-router-dom'
import { Security, ImplicitCallback, SecureRoute } from '@okta/okta-react';

import Login from '../Login'
import Home from '../Home'

class Main extends Component {
  render() {
    return (
      <p>Main</p>
    );
  }
}

export default Main;