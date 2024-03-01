import tkinter as tk


class AddWaypointsWindow(tk.Toplevel):
    def __init__(self, *args, vehicleDict, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.vd = vehicleDict
        self.callback = callback
        self.config(width=300, height=300)
        self.resizable(False, False)
        self.title("Vehicle Information")

        # get options for drop down menu
        options = self.loadOptions()

        # setup for drop down menu
        self.selected = tk.StringVar()
        self.selected.set(options[0])

        self.drop = tk.OptionMenu(self, self.selected, *options)
        self.drop.place(x=150, y=20)

        self.label_drop = tk.Label(self, text="Vehicle:")
        self.label_drop.place(x=50, y=20)

        self.label_tx = tk.Label(self, text="Tx")
        self.label_tx.place(x=50, y=60, width=130)

        self.entry_tx = tk.Entry(self)
        self.entry_tx.place(x=150, y=60, width=130)

        self.label_ty = tk.Label(self, text="Ty")
        self.label_ty.place(x=50, y=100, width=130)

        self.entry_ty = tk.Entry(self)
        self.entry_ty.place(x=150, y=100, width=130)

        self.label_rx = tk.Label(self, text="Rz")
        self.label_rx.place(x=50, y=140, width=130)

        self.entry_rx = tk.Entry(self)
        self.entry_rx.place(x=150, y=140, width=130)

        self.label_op = tk.Label(self, text="Op")
        self.label_op.place(x=50, y=180, width=130)

        self.entry_op = tk.Entry(self)
        self.entry_op.place(x=150, y=180, width=130)

        self.label_time = tk.Label(self, text="Order")
        self.label_time.place(x=50, y=220, width=130)

        self.entry_time = tk.Entry(self)
        self.entry_time.place(x=150, y=220, width=130)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=260, width=260)

        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        if self.selected.get() in self.vd:
            tx = float(self.entry_tx.get())
            ty = float(self.entry_ty.get())
            rx = float(self.entry_rx.get())
            op = float(self.entry_op.get())
            time = float(self.entry_time.get())

            vehicle = self.vd.get(self.selected.get())

            self.callback(vehicle, tx, ty, rx, op, time)

            # kill this window
            self.destroy()

    def loadOptions(self):
        out = ["Don't Select Me"]
        for key in self.vd.keys():
            out.append(key)
        if len(out) > 1:
            out.pop(0)
        return out
