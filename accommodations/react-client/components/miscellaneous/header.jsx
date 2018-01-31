import React from 'react';
import '../static/styles/components/header.css';

const Header = props => (
  <div className="column is-12" style={{ padding: '0', paddingBottom: '0.75rem' }}>
    <nav className="navbar is-transparent" style={{ backgroundImage: 'url("/static/images/header.png")', backgroundSize: 'cover', backgroundRepeat: 'no-repeat', width: '100%' }}>
      <div className="navbar-brand">
        <a className="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28" />
        </a>
        <div className="navbar-burger burger" data-target="navbarExampleTransparentExample">
          <span />
          <span />
          <span />
        </div>
      </div>

      <div id="navbarExampleTransparentExample" className="navbar-menu" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
        <div className="navbar-start">
          <a className="navbar-item" href="https://bulma.io/">Home</a>
          <div className="navbar-item has-dropdown is-hoverable">
            <a className="navbar-link" href="/documentation/overview/start/">Docs</a>
            <div className="navbar-dropdown is-boxed">
              <a className="navbar-item" href="/documentation/overview/start/">Overview</a>
              <a className="navbar-item" href="https://bulma.io/documentation/modifiers/syntax/">Modifiers</a>
              <a className="navbar-item" href="https://bulma.io/documentation/columns/basics/">Columns</a>
              <a className="navbar-item" href="https://bulma.io/documentation/layout/container/">Layout</a>
              <a className="navbar-item" href="https://bulma.io/documentation/form/general/">Form</a>
              <hr className="navbar-divider" />
              <a className="navbar-item" href="https://bulma.io/documentation/elements/box/">Elements</a>
              <a className="navbar-item is-active" href="https://bulma.io/documentation/components/breadcrumb/">Components</a>
            </div>
          </div>
          <a className="navbar-item" href="https://bulma.io/">FAQ</a>
        </div>

        <div className="navbar-end">
          <a className="navbar-item" href="#" onClick={props.signOut}>Sign Out</a>
        </div>

      </div>
    </nav>
  </div>
);

export default Header;
