import React from 'react';
import ReactDOM from 'react-dom';

// main app
import { Provider } from 'react-redux';
import AppRoutes from './routes.jsx';
import store from './store.jsx';

ReactDOM.render(
  <Provider store={store}>
    <AppRoutes />
  </Provider>,
  document.getElementById('app'),
);
