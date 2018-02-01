import React from 'react';

export default props => (
  <div className="card tile is-parent is-vertical is-3 card inline-block" style={{ padding: 0, margin: '10px' }} key={props.index}>
    <header className="card-header">
      <p className="card-header-title">{props.space.space_name}</p>
    </header>
    <div className="card-content" style={{ padding: 0 }}>
      <div className="content">
        <figure className="image is-4by3" style={{ margin: 0 }}>
          <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image" />
        </figure>
      </div>
    </div>
    <footer className="card-footer">
      <a href="#" className="card-footer-item">Photos</a>
      <a href="#" className="card-footer-item">Rooms</a>
      <a href="#" className="card-footer-item">Where</a>
    </footer>
  </div>
);
