import { HIDE_MODAL, SHOW_MODAL_FORM_ERROR } from '../types/modal.jsx';
import { SHOW_NOTIFICATION } from '../types/base.jsx';
import request from '../axios/axios.jsx';

function getSpace(id) {
  return request({
    url: `/message/${id}`,
    method: 'GET',
  });
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
