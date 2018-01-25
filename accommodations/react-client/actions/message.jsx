import { SET_MESSAGE } from '../types/message.jsx';

export const setMessage = (message) => {
  return dispatch => {
    dispatch({
      type: SET_MESSAGE,
      payload: {
        message
      }
    })
  }
}