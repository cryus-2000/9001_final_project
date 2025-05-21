# 📸 Photographer Task Manager

A command-line task manager for cosplay photographers to manage upcoming shoots, calculate pricing, and keep track of completed and uncompleted tasks. Built in Python using only standard libraries.

---

## Features

- Add a new photoshoot task
- View all tasks sorted by shoot date
- Delete a task by ID
- Update task details (e.g., location, time, number of people)
- Display statistics: total tasks, completion status, total price
- Persistent storage using JSON file
- Fully wrapped input validation

---

## Project Structure

```
PhotoTaskManager/
├── Task.py               # Task class definition
├── TaskManager.py        # TaskManager class for managing task list and file I/O
├── main.py               # Entry point with command-line menu interface
├── data.json             # Auto-generated file storing task data
└── README.md             # Project documentation
```

---

## How to Run

1. Ensure you're using **Python 3.x**.
2. Run the following command in your terminal:

```bash
python main.py
```

3. Follow the menu instructions to add, view, or update tasks.

> The `data.json` file will be created automatically on first use.

---

## Pricing Logic

- Base price: **100 AUD**
- +50 AUD for each additional person (first person is included)
- +30 AUD if the shoot is at **night**
- +20 AUD if the location is **outdoor**


## Sample Task Output

```
Task Summary - T3
-------------------------
number of people  : 2
time period       : night
location type     : outdoor
location detail   : Central Park
character         : Hatsune Miku
shoot date        : 2025-10-01
completed         : False
price             : 200
-------------------------
```
## Author

Xihang Cai  
COMP9001 Python final project  