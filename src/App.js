import React, { Component } from 'react';
import TodoListTemplate from './components/TodoListTemplate';
import TodoItemList from './components/TodoItemList';

class App extends Component {
  render() {
    return (
      <TodoListTemplate>
        <TodoItemList />
      </TodoListTemplate>
    );
  }
}

export default App;