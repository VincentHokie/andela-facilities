import { SPACES_RETRIEVED } from '../types/spaces.jsx';

const initState = {
  spaces: [],
};

export default (state = initState, action) => {
  switch (action.type) {
    case SPACES_RETRIEVED:
      return {
        ...state,
        spaces: action.payload,
      };
    default:
      return state;
  }
};
