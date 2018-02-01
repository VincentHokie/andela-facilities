import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import baseReducer from './reducers/notification.jsx';
import modalReducer from './reducers/modal.jsx';
import dataReducer from './reducers/data.jsx';

const reducer = combineReducers({
  baseReducer,
  modalReducer,
  dataReducer,
});

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

export default store;
