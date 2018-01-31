import { SHOW_NOTIFICATION, HIDE_NOTIFICATION } from '../types/notification.jsx';

const initState = {
  notification: false,
  notificationType: false,
};

export default (state = initState, action) => {
  switch (action.type) {
    case SHOW_NOTIFICATION:
      return {
        ...state,
        notification: action.payload.notification,
        notificationType: action.payload.notificationType,
      };
    case HIDE_NOTIFICATION:
      return {
        ...state,
        notification: false,
        notificationType: false,
      };
    default:
      return state;
  }
};
