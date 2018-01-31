import React from 'react';

const SpaceRecord = props => (
  <tr key={ props.index }>
    <th>{ props.index }</th>
    <td><abbr title="Picture">{ props.space_name }</abbr></td>
    <th><i className="fa fa-edit" aria-hidden="true"></i></th>
    <th><i className="fa fa-trash" aria-hidden="true"></i></th>
  </tr>
);

export default SpaceRecord;
