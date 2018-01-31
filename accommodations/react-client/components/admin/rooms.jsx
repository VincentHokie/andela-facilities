import React from 'react';
import Base from '../../containers/base.jsx';
import DashboardWrapper from '../../containers/dashboardHOC.jsx';

class Rooms extends Base {
  render() {
    return (
      <div>
        <h1 className="title is-4">Rooms</h1>
        <h2 className="subtitle is-6">You can use this page to manage rooms occupied by fellows in Andela Spaces.</h2>
        <table className="table" >
          <thead>
            <tr>
              <th>#</th>
              <th><abbr title="Picture">Space</abbr></th>
              <th>Room</th>
              <th><abbr title="Played">Capacity</abbr></th>
              <th><abbr title="Played">Available</abbr></th>
              <th>Edit</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tfoot>
            <tr>
              <th>#</th>
              <th><abbr title="Picture">Space</abbr></th>
              <th>Room</th>
              <th><abbr title="Played">Capacity</abbr></th>
              <th><abbr title="Played">Available</abbr></th>
              <th>Edit</th>
              <th>Delete</th>
            </tr>
          </tfoot>
          <tbody>
            <tr>
              <th>1</th>
              <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C." title="Leicester City F.C.">Leicester City</a> <strong>(C)</strong>
              </td>
              <td>38</td>
              <td>23</td>
              <td>12</td>
              <th><i className="fa fa-edit" aria-hidden="true"></i></th>
              <th><i className="fa fa-trash" aria-hidden="true"></i></th>
            </tr>
            <tr>
              <th>2</th>
              <td><a href="https://en.wikipedia.org/wiki/Arsenal_F.C." title="Arsenal F.C.">Arsenal</a></td>
              <td>38</td>
              <td>20</td>
              <td>11</td>
              <th><i className="fa fa-edit" aria-hidden="true"></i></th>
              <th><i className="fa fa-trash" aria-hidden="true"></i></th>
            </tr>
            <tr>
              <th>3</th>
              <td><a href="https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C." title="Tottenham Hotspur F.C.">Tottenham Hotspur</a></td>
              <td>38</td>
              <td>19</td>
              <td>13</td>
              <th><i className="fa fa-edit" aria-hidden="true"></i></th>
              <th><i className="fa fa-trash" aria-hidden="true"></i></th>
            </tr>
            <tr className="is-selected">
              <th>4</th>
              <td><a href="https://en.wikipedia.org/wiki/Manchester_City_F.C." title="Manchester City F.C.">Manchester City</a></td>
              <td>38</td>
              <td>19</td>
              <td>9</td>
              <th><i className="fa fa-edit" aria-hidden="true"></i></th>
              <th><i className="fa fa-trash" aria-hidden="true"></i></th>
            </tr>
            <tr>
              <th>5</th>
              <td><a href="https://en.wikipedia.org/wiki/Manchester_United_F.C." title="Manchester United F.C.">Manchester United</a></td>
              <td>38</td>
              <td>19</td>
              <td>9</td>
              <th><i className="fa fa-edit" aria-hidden="true"></i></th>
              <th><i className="fa fa-trash" aria-hidden="true"></i></th>
            </tr>
          </tbody>
        </table >
      </div>
    );
  }
}

export default DashboardWrapper(Rooms, {}, {});
