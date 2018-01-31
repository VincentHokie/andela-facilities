import React from 'react';

const Notification = props => (
  <div style={{ marginTop: '10px' }} className='columns is-mobile is-centered'>
    <div className={'notification column is-half-mobile is-two-thirds-tablet is-three-quarters-desktop is-three-fifths-widescreen is-three-fifths-fullhd ' + (props.notificationType && props.notificationType == 'success' ? 'is-success' : 'is-danger')}>
      <button className="delete" onClick={props.close}></button>
      {props.notification}
    </div>
  </div>
);

export default Notification;
