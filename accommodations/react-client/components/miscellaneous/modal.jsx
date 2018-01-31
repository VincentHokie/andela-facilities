import React from 'react';

const Modal = props => (

  <div className={props.active ? 'modal is-active' : 'modal'}>
    <form onSubmit={props.onSubmit}>
      <div className="modal-background" />
      <div className="modal-card">
        <header className="modal-card-head">
          <p className="modal-card-title">{props.title}</p>
          <button className="delete" aria-label="close" onClick={props.close} />
        </header>
        <section className="modal-card-body">
          {props.children}
        </section>
        <footer className="modal-card-foot">
          <button className="button is-success">{props.button}</button>
          <button className="button" onClick={props.close}>Cancel</button>
        </footer>
      </div>
    </form>
  </div>

);

export default Modal;
