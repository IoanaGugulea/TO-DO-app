// scripts.js

// Mark a task as completed
document.addEventListener("DOMContentLoaded", function () {
    const tasks = document.querySelectorAll(".task-list li");
    tasks.forEach(task => {
        task.addEventListener("click", function () {
            task.classList.toggle("completed");
        });
    });
});
