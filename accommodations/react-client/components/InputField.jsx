import React from 'react';

const InputField = props => (

  <div className="field">
    <label className="label">{props.label}</label>
    <div className="control has-icons-left has-icons-right">
      <input className={props.error ? 'input is-danger' : 'input'} type={props.type} name={props.name} />
      <span className="icon is-small is-left">
        <i className="fas fa-envelope" />
      </span>
      {props.error ?
        <span className="icon is-small is-right">
          <i className="fas fa-exclamation-triangle" style={{ color: 'red' }} />
        </span>
        : ''}
    </div>
    {props.error ? <p className="help is-danger">{ props.error }</p> : ''}
  </div>

);

export default InputField;
