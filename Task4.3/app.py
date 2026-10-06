from flask import Flask, render_template, request, redirect, url_for
import socket

app = Flask(__name__)

STUDENT_NAME = "Hoo Ying Kit"
STUDENT_ID = "105190469"

# In-memory Task Dataset
tasks = [
    {
        "id": 1,
        "title": "Finish Python App UI Mockup",
        "category": "Work",
        "priority": "High Priority",
        "due": "Today, 5:00 PM",
        "completed": False
    },
    {
        "id": 2,
        "title": "Review requirement for Project Brief",
        "category": "Work",
        "priority": "Normal",
        "due": "Oct 15",
        "completed": False
    },
    {
        "id": 3,
        "title": "Grocery shopping",
        "category": "Personal",
        "priority": "Low Priority",
        "due": "Nov 28",
        "completed": False
    },
    {
        "id": 4,
        "title": "Watch Drama",
        "category": "Personal",
        "priority": "Low Priority",
        "due": "Nov 29",
        "completed": False
    },
    {
        "id": 5,
        "title": "Completed Deployment Portfolio Task 3",
        "category": "Work",
        "priority": "High Priority",
        "due": "Sep 28",
        "completed": True
    }
]

@app.route("/")
def index():
    container_id = socket.gethostname()
    filter_type = request.args.get("filter", "all")

    # Filter tasks based on selected sidebar item
    if filter_type == "completed":
        filtered_tasks = [t for t in tasks if t["completed"]]
    elif filter_type in ["Work", "Personal", "Study"]:
        filtered_tasks = [t for t in tasks if t["category"] == filter_type]
    else:
        filtered_tasks = tasks

    # Dynamic counts for sidebar badges
    counts = {
        "all": len(tasks),
        "completed": len([t for t in tasks if t["completed"]]),
        "work": len([t for t in tasks if t["category"] == "Work"]),
        "personal": len([t for t in tasks if t["category"] == "Personal"]),
        "study": len([t for t in tasks if t["category"] == "Study"]),
    }

    return render_template("index.html", 
                           tasks=filtered_tasks, 
                           current_filter=filter_type,
                           counts=counts,
                           student_name=STUDENT_NAME, 
                           student_id=STUDENT_ID, 
                           container_id=container_id)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    category = request.form.get("category", "Work")
    priority = request.form.get("priority", "Normal")
    due = request.form.get("due", "Pending")

    if title:
        new_id = max([t["id"] for t in tasks], default=0) + 1
        tasks.append({
            "id": new_id,
            "title": title,
            "category": category,
            "priority": priority,
            "due": due if due else "No date",
            "completed": False
        })
    return redirect(url_for("index", filter=request.form.get("current_filter", "all")))

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    current_filter = request.args.get("filter", "all")
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index", filter=current_filter))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    current_filter = request.args.get("filter", "all")
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index", filter=current_filter))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)