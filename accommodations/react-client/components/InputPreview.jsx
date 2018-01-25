import React from 'react';

const InputPreview = props => (
  <div>
    <input type="text" value={props.value} onChange={e => props.onChange(e.target.value)} />
  </div>
);

export default InputPreview;
