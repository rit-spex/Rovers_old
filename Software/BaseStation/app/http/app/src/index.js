import React from 'react';
import ReactDOM from 'react-dom';
import { Router } from 'react-router-dom'
import { createBrowserHistory } from 'history'
import 'bootstrap/dist/css/bootstrap.min.css';

import Main from './Main';

const history = createBrowserHistory();

ReactDOM.render((
  <Router history={history}>
    <Main history={history} />
  </Router>
), document.getElementById('root'))