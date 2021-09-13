import React from 'react';
import './TodoListTemplate.css';
import update from '../update.png'

const TodoListTemplate = ({ children }) => {
  return (
    <main className="todo-list-template">
      <div>
        <div className="title" >ESXi VM Status</div>
          <a href="https://github.com/walt4771/ESX-VMList_React" className="right-update" >
          <img className="updateImg" src={update} />
          </a>
      </div>

      <div className="subtitle" >@walt4771</div>
      <section className="todos-wrapper">
        { children }
      </section>
    </main>
  );
};

export default TodoListTemplate;