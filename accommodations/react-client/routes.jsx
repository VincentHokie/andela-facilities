import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Login from './containers/Login.jsx';
import Home from './containers/home.jsx';

export default () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route path="/home" component={Home} />
      </Switch>
      <ToastContainer />
    </div>
  </BrowserRouter>
);
