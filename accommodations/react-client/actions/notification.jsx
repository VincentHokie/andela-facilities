import { HIDE_NOTIFICATION } from '../types/notification.jsx';

export const hideNotification = (event) => {
  event.preventDefault();
  return dispatch => (
    dispatch({
      type: HIDE_NOTIFICATION,
    })
  );
};

