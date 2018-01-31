import { SIGNIN_SUCCESS, SIGNOUT_SUCCESS } from '../types/auth.jsx';

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
    default:
      return state;
  }
};
