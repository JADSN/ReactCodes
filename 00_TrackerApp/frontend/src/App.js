// * Internal Imports
import { useState, useEffect } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

// * Components
import Header from "./components/Header";
import Tasks from "./components/Tasks";
import AddTask from "./components/AddTask";
import Footer from "./components/Footer";
import About from "./components/About";

function App() {
  const [showAddTask, setShowAddTask] = useState(false);
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const getTasks = async () => {
      const tasksFromServer = await fetchTasks();
      setTasks(tasksFromServer);
    };
    getTasks();
  }, []);

  // * Fetch all tasks
  const fetchTasks = async () => {
    const res = await fetch("http://localhost:5000/tasks");
    const data = await res.json();
    return data;
  };

  // * Fetch task by id
  const fetchTaskByid = async (id) => {
    const res = await fetch(`http://localhost:5000/tasks/${id}`);
    const data = await res.json();
    return data;
  };

  // * Add Task
  const addTask = async (task) => {
    // const randomId = Math.floor(Math.random() * 10000) + 1;
    // const newTask = { id: randomId, ...task };

    const body = JSON.stringify(task);

    await fetch(`http://localhost:5000/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json; charset=utf-8",
      },
      body: body,
    }).then(async (response) => {
      const respOk = await response.ok;
      if (respOk) {
        const newTask = await response.json();
        console.log(newTask);
        setTasks([...tasks, newTask]);
        alert("ADICIONADO");
      } else {
        alert("Tente adcionar novamente");
      }
    });
  };

  //  * Delete Task
  const deleteTask = async (id) => {
    await fetch(`http://localhost:5000/tasks/${id}`, { method: "DELETE" }).then(
      (response) => {
        if (response.ok) {
          setTasks(tasks.filter((task) => task.id !== id));
          alert("DELETADO");
        } else {
          alert("Tente deletar novamente");
        }
      }
    );
  };

  // * Toggle Reminder
  const toggleReminder = async (id) => {
    // console.log("TOGGLE: ", id);
    // setTasks(
    //   tasks.map((task) =>
    //     task.id === id ? { ...task, reminder: !task.reminder } : task
    //   )
    // );

    const taskToToggle = await fetchTaskByid(id);
    const updTask = { ...taskToToggle, reminder: !taskToToggle.reminder };

    await fetch(`http://localhost:5000/tasks/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json; charset=utf-8",
      },
      body: JSON.stringify(updTask),
    }).then(async (response) => {
      const respOk = await response.ok;
      if (respOk) {
        const updatedTask = await response.json();
        console.log(updatedTask);
        setTasks(
          tasks.map((task) =>
            task.id === id ? { ...task, reminder: updatedTask.reminder } : task
          )
        );
        alert("ATUALIZADO");
      } else {
        alert("Tente atualizar novamente");
      }
    });
  };

  return (
    <Router>
      <div className="container">
        <Header
          onAdd={() => setShowAddTask(!showAddTask)}
          showAdd={showAddTask}
        />
        <Route
          path="/"
          exact
          render={(props) => (
            <>
              {showAddTask && <AddTask onAddTask={addTask} />}
              {tasks.length > 0 ? (
                <Tasks
                  tasks={tasks}
                  onDelete={deleteTask}
                  onToggle={toggleReminder}
                />
              ) : (
                "No Tasks To Show"
              )}
            </>
          )}
        />
        <Route path="/about" component={About} />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
