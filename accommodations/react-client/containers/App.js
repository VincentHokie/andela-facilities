import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import InputPreview from '../components/InputPreview';
import { connect } from 'react-redux';
import { setMessage } from '../actions/message';
import Script from 'react-load-script';
import { signIn } from '../actions/auth'
import { bindActionCreators } from 'redux'

class App extends Component {
    _onChange = (value) => {
        this.props.dispatch(setMessage(value))
    }

    onSuccess = (googleUser) => {
        this.props.signIn(googleUser);
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

    signOut = () => {
        console.log("user signing out")
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
            console.log('User signed out.');
        });
    }

render() {
    {/*const { message } = this.props.messageReducer;*/}
    return (
        <div style={{ backgroundImage: 'url("/static/login-bg.jpg")', height: window.innerHeight, backgroundSize: "cover", backgroundRepeat: "no-repeat", width: "100%" }}>
            {/*<InputPreview value={message} onChange={this._onChange} />
            <Link to='/about'>
                <button>Go to About</button>
            </Link>*/}
            <a href="#" onClick={this.signOut}>Sign out</a>
            <center><div id="my-signin2"></div></center>
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
  )(App)
