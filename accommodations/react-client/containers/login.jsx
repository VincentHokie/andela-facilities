import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import Script from 'react-load-script';
import { signIn, signOut } from '../actions/auth.jsx'
import { bindActionCreators } from 'redux'
import Base from './base.jsx';
import { toast } from 'react-toastify';
import CustomToast from "../components/custom_toast.jsx";

class Login extends Base {

    onSuccess = (googleUser) => {
        this.props.signIn(googleUser, this.props, gapi);
    }

    signOut = (googleUser) => {
        this.props.signOut(this.props);
    }

    onFailure = (error) => {
        console.log(error);
    }

    renderButton = () => {
        gapi.signin2.render('my-signin2', {
            'scope': 'profile email',
            'width': 240,
            'height': 50,
            'longtitle': true,
            'theme': 'dark',
            'onsuccess': this.onSuccess,
            'onfailure': this.onFailure
        });
    }

render() {
    return (
        <div style={{ backgroundImage: 'url("/static/images/login-bg.jpg")', height: window.innerHeight, backgroundSize: "cover", backgroundRepeat: "no-repeat", width: "100%" }}>
            <center style={{ paddingTop: (window.innerHeight/2)-50 }}><div id="my-signin2"></div></center>
            <Script
                url="https://apis.google.com/js/platform.js"
                attributes={{ "async": "", "defer": "" }}
                onLoad={this.renderButton}
            />
        </div>
    )
}
}
  
  const mapDispatchToProps = dispatch => bindActionCreators({
    signIn,
  }, dispatch)
  
  export default connect(
    null,
    mapDispatchToProps
  )(Login)
