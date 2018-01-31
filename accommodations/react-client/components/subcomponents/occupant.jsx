import React from 'react';

const OccupantRecord = props => (
  <tr key={ props.index }>
    <th>{ props.index }</th>
    <td><abbr title="Picture">{props.space}</abbr></td>
    <td>{props.room}</td>
    <td><abbr title="Played">{props.email}</abbr></td>
    <td><abbr title="Played">{props.entry_date}</abbr></td>
    <td><abbr title="Played">{props.exit_date}</abbr></td>
    <th><i className="fa fa-edit" aria-hidden="true"></i></th>
    <th><i className="fa fa-trash" aria-hidden="true"></i></th>
  </tr>
);

export default OccupantRecord;
