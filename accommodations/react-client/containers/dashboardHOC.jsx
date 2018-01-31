import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import Header from '../components/miscellaneous/header.jsx';
import SideBar from '../components/miscellaneous/sidebar.jsx';
import { signOut } from '../actions/auth.jsx'
import Base from './base.jsx';
import { hideNotification } from '../actions/notification.jsx';
import InputField from '../components/InputField.jsx';
import Notification from '../components/miscellaneous/notification.jsx';

function DashboardWrapper(Component, passedActions, passedState) {
  class BaseFilter extends Base {

    signOut = () => {
      this.props.signOut(this.props);
    }

    render() {
      return (
        <div>
          <Header signOut={this.signOut} />
          <div className="columns">
            <SideBar push={this.pushNavigation} />
            <div className="column is-half-mobile is-two-thirds-tablet is-three-quarters-desktop is-four-fifths-widescreen is-four-fifths-fullhd">
              { this.props.notification && this.props.notificationType ? 
                <Notification notification={this.props.notification} notificationType={this.props.notificationType} close={this.props.hideNotification} /> : '' }
              <div className="column is-fullwidth">
                {Component ? <Component {...this.props} /> : ''}
              </div>
            </div>
          </div>
        </div>
      );
    }
  }

  const mapDispatchToProps = dispatch => bindActionCreators({
    signOut,
    hideNotification,
    ...passedActions,
  }, dispatch);

  const mapStateToProps = state => ({
    form: state.modalReducer.form,
    onSubmit: state.modalReducer.onSubmit,
    error: state.modalReducer.error,
    show: state.modalReducer.show,
    modalTitle: state.modalReducer.modalTitle,
    buttonLabel: state.modalReducer.buttonLabel,
    notification: state.baseReducer.notification,
    notificationType: state.baseReducer.notificationType,
    ...passedState,
  });

  return connect(
    mapStateToProps,
    mapDispatchToProps,
  )(BaseFilter);

}

export default DashboardWrapper;
