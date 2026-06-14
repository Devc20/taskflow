const API_URL = "/api/tasks";

const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const emptyState = document.getElementById("empty-state");

async function loadTasks() {
  const response = await fetch(API_URL);
  const tasks = await response.json();
  renderTasks(tasks);
}

async function addTask(text) {
  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  await loadTasks();
}

async function toggleTask(taskId, isDone) {
  await fetch(`${API_URL}/${taskId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ is_done: isDone }),
  });
  await loadTasks();
}

async function deleteTask(taskId) {
  await fetch(`${API_URL}/${taskId}`, { method: "DELETE" });
  await loadTasks();
}

function renderTasks(tasks) {
  taskList.innerHTML = "";
  emptyState.classList.toggle("empty-state--hidden", tasks.length > 0);

  for (const task of tasks) {
    taskList.appendChild(createTaskElement(task));
  }
}

function createTaskElement(task) {
  const item = document.createElement("li");
  item.className = "task-item";
  if (task.is_done) {
    item.classList.add("task-item--done");
  }

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "task-item__checkbox";
  checkbox.checked = task.is_done;
  checkbox.addEventListener("change", () => toggleTask(task.id, checkbox.checked));

  const text = document.createElement("span");
  text.className = "task-item__text";
  text.textContent = task.text;

  const deleteButton = document.createElement("button");
  deleteButton.className = "task-item__delete";
  deleteButton.textContent = "×";
  deleteButton.setAttribute("aria-label", "Borrar tarea");
  deleteButton.addEventListener("click", () => deleteTask(task.id));

  item.append(checkbox, text, deleteButton);
  return item;
}

taskForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const text = taskInput.value.trim();
  if (text === "") {
    return;
  }
  addTask(text);
  taskInput.value = "";
});

loadTasks();
