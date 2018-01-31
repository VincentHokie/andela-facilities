import React from 'react';

const UserRecord = props => (
  <tr key={ props.index }>
    <th>{ props.index }</th>
    <td><abbr title="Picture">{ props.appuser_picture }</abbr></td>
    <td>{ props.username }</td>
    <td><abbr title="Played">{ props.first_name } { props.last_name }</abbr></td>
    <td><abbr title="Won">{ props.email }</abbr></td>
    <td><abbr title="Drawn">{ props.access }</abbr></td>
    <th><i className="fa fa-edit" aria-hidden="true"></i></th>
    <th><i className="fa fa-trash" aria-hidden="true"></i></th>
  </tr>
);

export default UserRecord;
