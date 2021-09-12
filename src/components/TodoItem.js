import React, { Component } from 'react';
import './TodoItem.css';


class TodoItem extends Component {
  render() {
    const { VMID, VMName, isPoweredOn } = this.props;
    const link = "https://{ESXi Host IP}/ui/#/host/vms/" + VMID
    return (
      <a href={link}>
      <div className="todo-item">
        <div className="left">
            <div style={{fontWeight:'bold'}}>{VMName}</div>
        </div>
        <div className="left-2">
            <div style={{fontWeight:'lighter', fontSize:12}}>{VMID}</div>
        </div>
        <div className="right_circle" 
            style={{backgroundColor: (isPoweredOn === "red") ? "#E6E9ED" : "#1CB63E"}}>
        </div>
      </div>
      </a>
    );
  }
}

export default TodoItem;