import React from 'react';
import axios from 'axios';
import { toast } from 'react-toastify';
import { SIGNIN_FAILURE, SIGNIN_SUCCESS, SIGNOUT_SUCCESS } from '../types/auth.jsx';
import CustomToast from "../components/custom_toast.jsx";

const logout = (dispatch, gapi, props, showToast=false) => {
  const googleAuth = gapi.auth2.getAuthInstance();
  return googleAuth.signOut().then(() => {
    // on successful logout

    // rediect the user
    setTimeout(() => {
      props.history.push('/');
    }, 1000);

    // show sign out success message
    if (showToast) {
      toast(<CustomToast message="Sign out successful!" />);
    }

    dispatch({
      type: SIGNOUT_SUCCESS,
    });
  });
};

export const signIn = (googleUser, props, googleApi) => {
  return dispatch => (
    axios.post('http://127.0.0.1:8000/accounts/auth/register/', { ID_Token: googleUser.getAuthResponse().id_token }, {
      headers: {},
    })
      .then((data) => {
        const { user, token } = data.data;

        axios.defaults.headers.common.Authorization = `jwt ${token}`;

        // show a success message
        toast(<CustomToast message="You have successfully signed in" />);

        // update state
        dispatch({
          type: SIGNIN_SUCCESS,
          payload: {
            user,
            token,
            gapi: googleApi,
          },
        });

        // rediect the user
        setTimeout(() => {
          props.history.push('/home');
        }, 1000);
      })
      .catch((err) => {

        // show error message
        toast(<CustomToast message="Login failed! Ensure you have an Andela mail" />);

        // ensure google user is logged out
        logout(dispatch, googleApi, props);
        dispatch({
          type: SIGNIN_FAILURE,
        });
      })
  );
};

export const signOut = (props) => {
  return (dispatch, getState) => {
    const { gapi } = getState().baseReducer;

    // log user out
    return logout(dispatch, gapi, props, true);
  };
};
