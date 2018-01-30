import React, { Component } from 'react';

class Base extends Component {

  pushNavigation = (event) => {
      event.preventDefault();
    this.props.history.push(event.target.getAttribute("href"));
  }

}


export default Base
