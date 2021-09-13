import React, { Component } from 'react';
import TodoItem from './TodoItem';

import data from "../vmlist.json"

class TodoItemList extends Component {
  render() {
    // const { } = this.props;
    
    for (var i = 0; i < 5; i++) { 
      if (data[i].isPoweredOn === "Powered on") {
        data[i].isPoweredOn = "blue"
      } else {
        data[i].isPoweredOn = "red"
      }
    }

    // let items = "";
    // for (var i = 0; i < 5; i++) {
    //   console.log(i)
    //   items += `<TodoItem VMName=${data[i].VMName} VMID=${data[i].VMID} isPoweredOn=${data[i].isPoweredOn} />`
    // }
    // console.log(items)

    return (
      <div>
        <div style={{ color: "#ffffff" }}>
            .
        </div>
        <TodoItem VMName={data[0].VMName} VMID={data[0].VMID} isPoweredOn={data[0].isPoweredOn} />
        <TodoItem VMName={data[1].VMName} VMID={data[1].VMID} isPoweredOn={data[1].isPoweredOn} />
        <TodoItem VMName={data[2].VMName} VMID={data[2].VMID} isPoweredOn={data[2].isPoweredOn} />
        <TodoItem VMName={data[3].VMName} VMID={data[3].VMID} isPoweredOn={data[3].isPoweredOn} />
        <TodoItem VMName={data[4].VMName} VMID={data[4].VMID} isPoweredOn={data[4].isPoweredOn} />
        <div style={{fontWeight:"lighter", textAlign:"center", color: "#868e96", padding:"15px"}}>
          You need to log in to see more details
        </div>
      </div>
    );
  }
}

export default TodoItemList;
