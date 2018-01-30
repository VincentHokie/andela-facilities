import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import Header from '../components/header.jsx';
import SideBar from '../components/sidebar.jsx';
import { signOut } from '../actions/auth.jsx'
import Base from './base.jsx';
import InputField from '../components/InputField.jsx';
import DashboardWrapper from './dashboardHOC.jsx';

class Home extends Base {

}

export default DashboardWrapper(Home, {}, {});
