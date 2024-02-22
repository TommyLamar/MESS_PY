import tkinter as tk
class ExpInputWindow(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        width = 300
        self.callback = callback
        self.config(width=width, height=110)
        self.resizable(False, False)
        self.title("Experiment Info")

        # setting up features
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=20, y=40, width=260)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=70, width=260)

        self.label_entry = tk.Label(self, text="Enter Experiment Name")
        self.label_entry.place(x=80, y=10)

        # make this the highlighted window
        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        self.callback(self.entry_name.get())

        # allow others to be grabbed
        self.grab_release()

        # kill this window
        self.destroy()
