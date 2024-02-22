import tkinter as tk


class AddSensorInput(tk.Toplevel):
    def __init__(self, *args, vehicleDict, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.vd = vehicleDict
        self.config(width=400, height=210)
        self.resizable(False, False)
        self.title("Sensor Information")

        # get options for drop down menu
        options = self.loadOptions()

        # setup for drop down menu
        self.selected = tk.StringVar()
        self.selected.set(options[0])

        self.drop = tk.OptionMenu(self, self.selected, *options)
        self.drop.place(x=150, y=10)

        self.label_drop = tk.Label(self, text="Sensor Location:")
        self.label_drop.place(x=50, y=10)

        self.refreshRateEntry = tk.Entry(self)
        self.refreshRateEntry.place(x=150, y=50, width=130)

        self.label_refreshRate = tk.Label(self, text="Refresh Rate:")
        self.label_refreshRate.place(x=50, y=50)

        self.packageButton = tk.Button(self, text="Select File", command=self.select_file_pressed)
        self.packageButton.place(x=150, y=120, width=130)

        self.label_rosPackage = tk.Label(self, text="ROS Package:")
        self.label_rosPackage.place(x=50, y=120)

        self.label_file = tk.Label(self, text="no file selected")
        self.label_file.place(x=10, y=150)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=180, width=260)

        self.nameEntry = tk.Entry(self)
        self.nameEntry.place(x=150, y=80, width=130)

        self.label_name = tk.Label(self, text="Sensor Name:")
        self.label_name.place(x=50, y=80)

        self.package = ""

        self.focus()

    def done_pressed(self):
        rr = int(self.refreshRateEntry.get())
        p = self.package
        vehicle = self.selected.get()
        name = self.nameEntry.get()
        # Use callback function to return to main window
        self.callback(p, rr, vehicle, name)

        # kill this window
        self.destroy()

    def select_file_pressed(self):
        name = fd.askopenfilename()
        self.package = name
        self.label_file.config(text=name)
        print(name)
        # need to actually process this into a usable format for the script

    # create list with all the vehicle names
    def loadOptions(self):
        out = ["Environmental"]
        for key in self.vd.keys():
            out.append(key)
        return out
