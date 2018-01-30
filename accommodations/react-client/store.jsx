import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import baseReducer from './reducers/base.jsx';
import modalReducer from './reducers/modal.jsx';

const reducer = combineReducers({
  baseReducer,
  modalReducer,
});

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

export default store;
