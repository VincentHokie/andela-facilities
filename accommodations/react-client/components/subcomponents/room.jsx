import React from 'react';

const RoomRecord = props => (
  <tr key={ props.index }>
    <th>{ props.index }</th>
    <td><abbr title="Picture">{ props.space }</abbr></td>
    <td>{ props.room }</td>
    <td><abbr title="Played">{ props.capacity }</abbr></td>
    <td><abbr title="Played">{ props.available }</abbr></td>
    <th><i className="fa fa-edit" aria-hidden="true"></i></th>
    <th><i className="fa fa-trash" aria-hidden="true"></i></th>
  </tr>
);

export default RoomRecord;
