import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import Header from '../components/header.jsx';
import SideBar from '../components/sidebar.jsx';
import { signOut } from '../actions/auth.jsx'
import Base from './base.jsx';
import InputField from '../components/InputField.jsx';


class About extends Base {

  signOut = () => {
    this.props.signOut(this.props);
  }

  spaceForm = () => {
    let space = { "space_name": "this field is required!" };
    return (
      <InputField name="space_name" type="text" label="Space Name" error={space} />
    )
  }

  render() {
    return (
      <div>
        <Header signOut={this.signOut} />
        <div className="columns">
          <SideBar />
          <div className="column">
            {this.props.notification && this.props.notificationType ?
              <div className="columns is-mobile is-centered">
                <div className={"notification column is-half-mobile is-two-thirds-tablet is-three-quarters-desktop is-three-fifths-widescreen is-three-fifths-fullhd " + (this.props.notificationType && this.props.notificationType == 'success' ? 'is-success' : 'is-danger')}>
                  <button className="delete" onClick={this.props.closeNotification}></button>
                  {this.props.notification}
                </div>
              </div>
              : ''}

          </div>
        </div>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => bindActionCreators({
  signOut,
}, dispatch);

const mapStateToProps = state => ({
  form: state.modalReducer.form,
  onSubmit: state.modalReducer.onSubmit,
  error: state.modalReducer.error,
  show: state.modalReducer.show,
  modalTitle: state.modalReducer.modalTitle,
  buttonLabel: state.modalReducer.buttonLabel,
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(About);

