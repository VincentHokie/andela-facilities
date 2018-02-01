import React from 'react';
import Base from './base.jsx';
import DashboardWrapper from './dashboardHOC.jsx';
import SpaceService from '../actions/spaceService.jsx';
import SpaceCard from '../components/spaceCard.jsx';

class Home extends Base {
  componentDidMount() {
    this.props.getSpace();
  }

  render() {
    return (
      <div className="columns">
        <div className="tile is-ancestor is-12" style={{ flexWrap: 'wrap' }}>
          {this.props.spaces ? this.props.spaces.map((space, i) => (
            <SpaceCard space={space} index={i} />
          )) : ''
          }
        </div>
      </div>
    );
  }
}

export default DashboardWrapper(
  Home,
  { ...SpaceService },
  state => ({
    spaces: state.dataReducer.spaces,
  }));
