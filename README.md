# Todo List

A small desktop todo list built with Python's Tkinter GUI toolkit. Tasks are saved in a `.todo` text file in the directory where you run the app, with one task per line.

## Requirements

- Python 3
- Tkinter (usually included with Python; some Linux distributions package it separately)

## Run

From the project directory, run:

```bash
python3 todoapp.py
```

## Developer instructions

The application lives entirely in `todoapp.py`. It has no third-party
dependencies, build step, or automated test suite.

### Development workflow

1. Make changes in `todoapp.py`.
2. Check that the file is syntactically valid:

   ```bash
   python3 -m py_compile todoapp.py
   ```

3. Launch the app with `python3 todoapp.py` and manually verify the affected
   interaction.

### Code conventions

- Keep the UI code in `TodoApp` and use `main()` only to create and run the
  Tkinter root window.
- Store tasks as `[text, completed]` pairs in `self.todos`; call `refresh()`
  after changing task data so the listbox stays in sync.
- Preserve keyboard support: the **Enter** key adds a task and a double-click
  toggles its completion state.
- Keep the project dependency-free unless a new dependency is necessary and
  documented in the Requirements section.

## Use

- Enter a task and press **Enter** or click **Add**.
- Select a task and click **Mark done / undo**, or double-click it, to toggle its completion state.
- Select a task and click **Remove** to delete it.
