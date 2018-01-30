import {
  SHOW_MODAL, HIDE_MODAL,
  SHOW_MODAL_FORM_ERROR, HIDE_MODAL_FORM_ERROR } from '../types/modal.jsx';

const initState = {
  form: '',
  onSubmit: () => { },
  error: {},
  show: false,
  modalTitle: '',
  buttonLabel: '',
};

export default (state = initState, action) => {
  switch (action.type) {
    case SHOW_MODAL:
      return {
        ...state,
        form: action.payload.form,
        onSubmit: action.payload.onSubmit,
        error: {},
        modalTitle: action.payload.modalTitle,
        buttonLabel: action.payload.buttonLabel,
        show: true,
      };
    case HIDE_MODAL:
      return {
        ...state,
        show: false,
      };
    case SHOW_MODAL_FORM_ERROR:
      return {
        ...state,
        error: action.payload.error,
      };
    case HIDE_MODAL_FORM_ERROR:
      return {
        ...state,
        error: {},
      };
    default:
      return state;
  }
};
