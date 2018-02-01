import { HIDE_MODAL, SHOW_MODAL_FORM_ERROR } from '../types/modal.jsx';
import { SHOW_NOTIFICATION, HIDE_NOTIFICATION } from '../types/notification.jsx';
import { SPACES_RETRIEVED } from '../types/spaces.jsx';
import request from '../axios/axios.jsx';

function getSpace() {
  return (dispatch) => {
    dispatch({
      type: SHOW_NOTIFICATION,
      payload: {
        notification: 'Getting the Andela spaces.',
        notificationType: 'success',
      },
    });

    return request({
      url: '/accommodation/space/',
      method: 'GET',
    }).then((data) => {
      // update state
      dispatch({
        type: SPACES_RETRIEVED,
        payload: data,
      });

      dispatch({
        type: HIDE_NOTIFICATION,
      });
    }).catch((error) => {
      dispatch({
        type: SHOW_NOTIFICATION,
        payload: {
          notification: error.data.detail ? error.data.detail : 'Something went wrong, please refresh the page.',
          notificationType: 'error',
        },
      });
    });
  };
}

function createSpace(event) {
  event.preventDefault();
  const formData = new FormData(event.target);

  return dispatch => (
    request({
      url: '/accommodation/space/create/',
      method: 'POST',
      data: formData,
    }).then((data) => {
      // update state
      dispatch({
        type: HIDE_MODAL,
      });

      dispatch({
        type: SHOW_NOTIFICATION,
        payload: {
          notification: 'The space has been successfully created.',
          notificationType: 'success',
        },
      });
    }).catch((error) => {
      dispatch({
        type: SHOW_MODAL_FORM_ERROR,
        payload: { error: error.data.formError },
      });
    })
  );
}

const MessageService = {
  getSpace, createSpace, // , update, delete, etc. ...
};

export default MessageService;
