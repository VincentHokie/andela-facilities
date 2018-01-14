import axios from 'axios';
import { SIGNIN_FAILURE, SIGNIN_SUCCESS, SIGNOUT_SUCCESS } from '../types/auth';

export const signIn = (googleUser) => {
  return dispatch => (
    axios.post('http://127.0.0.1:8000/accounts/auth/register/', { ID_Token : googleUser.getAuthResponse().id_token })
      .then(({ data: { token, user }}) => {
        dispatch({
          type: SIGNIN_SUCCESS,
          payload: user,
        });
      })
      .catch((err) => {
        dispatch({
          type: SIGNIN_FAILURE,
        });
      })
  )
};

export const signOut = () => {
  return dispatch => {
    const googleAuth = gapi.auth2.getAuthInstance();

    return googleAuth.signOut().then(() => {
      dispatch({
        type: SIGNIN_SUCCESS,
      });
    });
  }
};
