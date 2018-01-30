import React from 'react';
import InputField from '../components/InputField.jsx';

export const newSpace = {

  form: props => (
    <div>
      <InputField name="space_name" type="text" label="Space Name" error={props && props.space_name ? props.space_name[0] : ''} />
    </div>
  ),
  onSubmit: 'createSpace',
  error: {},
  show: true,
  modalTitle: 'New Space Form',
  buttonLabel: 'Save Space',

};
