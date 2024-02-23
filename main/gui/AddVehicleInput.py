import tkinter as tk


# Window that pops up to add a vehicle to an experiment
class AddVehicleInput(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.config(width=300, height=110)
        self.resizable(False, False)
        self.title("Vehicle Information")

        # set up features
        self.vehicleNameEntry = tk.Entry(self)
        self.vehicleNameEntry.place(x=150, y=20, width=130)

        self.label_name = tk.Label(self, text="Vehicle Name:")
        self.label_name.place(x=50, y=20)

        self.vehicleIPEntry = tk.Entry(self)
        self.vehicleIPEntry.place(x=150, y=40, width=130)

        self.label_ip = tk.Label(self, text="IP Address:")
        self.label_ip.place(x=50, y=40)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=80, width=260)

        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        self.callback(self.vehicleNameEntry.get(), self.vehicleIPEntry.get())

        # allows other to grab
        self.grab_release()

        # kill this window
        self.destroy()
