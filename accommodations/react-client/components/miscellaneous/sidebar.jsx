import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import '../static/styles/components/sidebar.css';
import Modal from '../components/modal.jsx';
import Base from '../containers/base.jsx';
import { showNewSpaceForm, hideModal } from '../actions/modalForm.jsx';
import SpaceService from '../actions/spaceService.jsx';

class SideBar extends Base {
  render() {
    return (
      <div className="column is-half-mobile is-one-third-tablet is-one-quarter-desktop is-one-fifth-widescreen is-one-fifth-fullhd">
        <aside className="menu">
          <p className="menu-label">General</p>
          <ul className="menu-list">
            <li><a href="/users" onClick={this.props.push}>Users & Permisisons</a></li>
          </ul>

          <p className="menu-label">Space
      <i className="fa fa-plus-circle" aria-hidden="true" onClick={this.props.showNewSpaceForm}></i>
          </p>
          <ul className="menu-list">
            <li><a href="/spaces/view" onClick={this.props.push}>See spaces</a></li>
          </ul>
          <p className="menu-label">Rooms
      <i className="fa fa-plus-circle" aria-hidden="true"></i>
          </p>
          <ul className="menu-list">
            <li><a href="/rooms/view" onClick={this.props.push}>View Rooms</a></li>
          </ul>
          <p className="menu-label">Assign Rooms
      <i className="fa fa-plus-circle" aria-hidden="true"></i>
          </p>
          <ul className="menu-list">
            <li><a href="/occupants/view" onClick={this.props.push}>View Occupants</a></li>
          </ul>
          <p className="menu-label">General</p>
          <ul className="menu-list">
            <li><a>Dashboard</a></li>
          </ul>
        </aside>

        <Modal
          active={this.props.show}
          onSubmit={this.props[this.props.onSubmit]}
          title={this.props.modalTitle}
          button={this.props.buttonLabel}
          close={this.props.hideModal}
          error={this.props.error}>
          { this.props.form ? this.props.form(this.props.error) : '' }
        </Modal>
      </div>

    );
  }

}

const mapDispatchToProps = dispatch => bindActionCreators({
  showNewSpaceForm,
  hideModal,
  ...SpaceService,
}, dispatch);

const mapStateToProps = state => ({
  form: state.modalReducer.form,
  error: state.modalReducer.error,
  onSubmit: state.modalReducer.onSubmit,
  show: state.modalReducer.show,
  modalTitle: state.modalReducer.modalTitle,
  buttonLabel: state.modalReducer.buttonLabel,
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(SideBar);
