import React from 'react';
import Base from '../../containers/base.jsx';
import DashboardWrapper from '../../containers/dashboardHOC.jsx';
import SpaceService from '../../actions/spaceService.jsx';
import SpaceRow from '../subcomponents/space.jsx';

class Spaces extends Base {
  componentDidMount() {
    this.props.getSpace();
  }

  render() {
    return (
      <div>
        <h1 className="title is-4">Andela Space</h1>
        <h2 className="subtitle is-6">You can use this page to manage spaces used by fellows under the facilities department.</h2>
        <table className="table" >
          <thead>
            <tr>
              <th>#</th>
              <th><abbr title="Picture">Space Name</abbr></th>
              <th>Edit</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tfoot>
            <tr>
              <th>#</th>
              <th><abbr title="Picture">Space Name</abbr></th>
              <th>Edit</th>
              <th>Delete</th>
            </tr>
          </tfoot>
          <tbody>
            {this.props.spaces ? this.props.spaces.map((space, i) => (
              <SpaceRow space={space} index={i} />
            )) : ''
            }
          </tbody>
        </table >
      </div>
    );
  }
}

export default DashboardWrapper(
  Spaces,
  { ...SpaceService },
  state => ({
    spaces: state.dataReducer.spaces,
  }));
