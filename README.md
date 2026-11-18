# To-Do List Manager CLI

A modular, lightweight command-line interface (CLI) application written in Python to manage everyday tasks.

---

## Architecture & Module Design

The application follows the Separation of Concerns (SoC) principle by dividing responsibilities across modular layers:

- `task.py` (Data Model): Defines the `Task` entity, its state, and serialization helpers (`to_dict` / `from_dict`).
- `task_manager.py` (Business Logic & Persistence): Manages in-memory task collections, handles IDs, and reads/writes state to `tasks.json`.
- `cli.py` (User Interface): Manages terminal presentation, user prompt loops, and input validation.
- `main.py` (Entry Point): Bootstrap file initiating the CLI session.

```
+---------------------------------------------------------+
|                        main.py                          |
+----------------------------+----------------------------+
                             |
                             v
+---------------------------------------------------------+
|                         cli.py                          |
|  - Renders menu options                                 |
|  - Validates user input format                          |
+----------------------------+----------------------------+
                             |
                             v
+---------------------------------------------------------+
|                    task_manager.py                      |
|  - add_task, remove_task, mark_completed               |
|  - JSON serialization / deserialization                 |
+----------------------------+----------------------------+
            |                               |
            v                               v
+-----------------------+       +-------------------------+
|        task.py        |       |       tasks.json        |
|  - Task object model  |       |  - Persistent storage   |
+-----------------------+       +-------------------------+
```

---

## Application Logic Flow (Pseudo-Code)

```
START application
    INITIALIZE TaskManager
    LOAD existing tasks from tasks.json (if present)
    
    LOOP FOREVER:
        DISPLAY main menu (1: View, 2: Add, 3: Complete, 4: Remove, 5: Exit)
        RECEIVE user choice
        
        IF choice == 1:
            FETCH all tasks
            DISPLAY tasks with status indicators ([ ] or [X])
            
        ELSE IF choice == 2:
            PROMPT for title
            VALIDATE title is non-empty
            GENERATE unique task ID
            SAVE updated list to tasks.json
            
        ELSE IF choice == 3:
            DISPLAY current tasks
            PROMPT for task ID
            VALIDATE ID is positive integer
            UPDATE task status to True
            SAVE updated list to tasks.json
            
        ELSE IF choice == 4:
            DISPLAY current tasks
            PROMPT for task ID
            VALIDATE ID is positive integer
            REMOVE task from collection
            SAVE updated list to tasks.json
            
        ELSE IF choice == 5:
            DISPLAY exit message
            TERMINATE process
            
        ELSE:
            DISPLAY invalid option error
```

---

## Prerequisites & Installation

- Python 3.8 or higher.
- No third-party packages required. The application uses only Python standard library modules (`sys`, `os`, `json`).

---

## How to Run

1. Extract the ZIP archive:
   ```bash
   unzip todo_list_manager.zip
   cd todo_list_manager
   ```

2. Run the application:
   ```bash
   python main.py
   ```
   *(Or `python3 main.py` depending on your environment).*

---

## Manual Testing Scenarios

1. **Viewing an Empty List**:
   - Start the program with no `tasks.json` file.
   - Choose option `1`.
   - Expected: Informative message indicating the list is empty.

2. **Input Validation on Add**:
   - Choose option `2` and press Enter without typing text.
   - Expected: Error message warning that task description cannot be blank.

3. **Adding Tasks**:
   - Add task "Complete Python assignment".
   - Add task "Review modular design concepts".
   - Choose option `1`. Both tasks appear with status `[ ]`.

4. **Marking a Task as Completed**:
   - Choose option `3`.
   - Enter `1`.
   - Choose option `1` to view tasks. Task 1 now displays `[X]`.

5. **Invalid ID Validation**:
   - Choose option `3` or `4` and enter non-numeric text (e.g., `abc`).
   - Expected: Friendly error stating a numerical ID is required without crashing.
   - Enter an out-of-range ID (e.g., `999`).
   - Expected: Friendly error indicating task does not exist.

6. **Removing a Task**:
   - Choose option `4`. Enter `1`.
   - Task 1 is removed. Choose option `1` to verify only task 2 remains.

7. **Persistence Verification**:
   - Exit the app (option `5`).
   - Relaunch `python main.py` and choose option `1`.
   - Expected: All tasks and completion statuses persist.
