import React, { Component } from 'react';

import { BrowserRouter as Router, Route, } from 'react-router-dom'

import RoverView from '../RoverView/index.js';
import ArmView from '../ArmView/index.js';
import Header from '../Header/index.js';
import HomeView from '../HomeView/index.js';


class Main extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <div className="containter">
            <Header />
            <Route path="/RoverView" render={props => (
              <React.Fragment>
                <RoverView />
              </React.Fragment>
            )} />
            <Route path="/ArmView" render={props => (
              <React.Fragment>
                <ArmView />
              </React.Fragment>
            )} />
            <Route exact path="/" render={props => (
              <React.Fragment>
                <HomeView />
              </React.Fragment>
            )} />
          </div>
        </div>
      </Router>
    );
  }
}

//document.getElementById("li_rover_view").addEventListener("click",)

export default Main;