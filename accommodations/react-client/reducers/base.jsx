import { SIGNIN_SUCCESS, SIGNOUT_SUCCESS } from '../types/auth.jsx';
import { SHOW_NOTIFICATION, HIDE_NOTIFICATION } from '../types/base.jsx';

const initState = {
  token: '',
  user: {},
  gapi: undefined,
  notification: false,
  notificationType: false,
};

export default (state = initState, action) => {
  switch (action.type) {
    case SIGNIN_SUCCESS:
      return {
        ...state,
        token: action.payload.token,
        user: action.payload.user,
        gapi: action.payload.gapi,
      };
    case SIGNOUT_SUCCESS:
      return {
        ...state,
        token: '',
        user: {},
      };
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
