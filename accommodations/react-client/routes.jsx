import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Login from './containers/Login.jsx';
import Home from './containers/home.jsx';
import Users from './components/usersAndPermissions.jsx';
import Spaces from './components/spaces.jsx';
import Rooms from './components/rooms.jsx';
import Occupants from './components/occupants.jsx';

export default () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route path="/home" component={Home} />
        <Route path="/users" component={Users} />
        <Route path="/spaces/view" component={Spaces} />
        <Route path="/rooms/view" component={Rooms} />
        <Route path="/occupants/view" component={Occupants} />
      </Switch>
      <ToastContainer />
    </div>
  </BrowserRouter>
);
