import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../components/header.jsx';

export default class About extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <p>About</p>
        <Link to='/'>
          <button>Go Home</button>
        </Link>
      </div>
    )
  }
}