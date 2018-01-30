import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Login from './containers/Login.jsx';
import About from './containers/About.jsx';

export default () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route path="/about" component={About} />
      </Switch>
      <ToastContainer />
    </div>
  </BrowserRouter>
);
