import { SHOW_MODAL, HIDE_MODAL } from '../types/modal.jsx';
import { newSpace } from '../components/modalFoms.jsx';

export const hideModal = (event) => {
  event.preventDefault();
  return dispatch => (
    dispatch({
      type: HIDE_MODAL,
    })
  );
};

export const showNewSpaceForm = () => (
  dispatch => (
    dispatch({
      type: SHOW_MODAL,
      payload: { ...newSpace },
    })
  )
);

export const showNewRoomForm = () => (
  dispatch => (
    dispatch({
      type: SHOW_MODAL,
      payload: newSpace(),
    })
  )
);
