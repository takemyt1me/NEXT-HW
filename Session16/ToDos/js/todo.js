const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
const content = document.querySelector("#content");
let todoArr = [];
const key = "TODOs";

function submitAddTodo(event) {
  event.preventDefault();
  const todoObj = {
    text: content.value,
    id: Date.now(),
  };
  todoArr.push(todoObj);
  saveTodos();
  paintTodo(todoObj);
  content.value = "";
}
todoForm.addEventListener("submit", submitAddTodo);

function deleteTodo(event) {
  const li = event.target.parentElement;
  li.remove();
  const id = parseInt(li.id);
  todoArr = todoArr.filter((todo) => todo.id !== id);
  saveTodos();
}

function paintTodo(todo) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = todo.text;
  const button = document.createElement("button");
  button.innerText = "X";
  button.addEventListener("click", deleteTodo);
  const todoList = document.getElementById("todo-list");
  todoList.appendChild(li);
  li.appendChild(span);
  li.appendChild(button);
  li.id = todo.id;
}

function saveTodos() {
  localStorage.setItem(key, JSON.stringify(todoArr));
}

function loadTodos() {
  const savedTodos = localStorage.getItem(key);
  if (savedTodos) {
    todoArr = JSON.parse(savedTodos);
    todoArr.forEach((todo) => paintTodo(todo));
  }
}

loadTodos();
