import tkinter as tk


class ViewVehicleWindow(tk.Toplevel):
    def __init__(self, *args, name, vehicleDict, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=600, height=300)
        title = name + "- Vehicles"
        self.title(title)

        self.vd = vehicleDict

        # get options for drop down menu
        options = self.loadOptions()

        # setup for drop down menu
        self.selected = tk.StringVar()
        self.selected.set(options[0])

        self.drop = tk.OptionMenu(self, self.selected, *options)
        self.drop.place(x=20, y=20)

        self.viewInfoButton = tk.Button(self, text="View Info", command=self.loadText)
        self.viewInfoButton.place(x=150, y=20)

        # screen elements
        self.bar = tk.Scrollbar(self)
        self.text = tk.Text(self, height=10, width=60)
        self.text.place(x=20, y=70)
        self.bar.place(x=510, y=70, height=200)
        self.bar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.bar.set)

        self.focus()
        self.grab_set()

    def loadOptions(self):
        out = ["Don't Select Me"]
        for key in self.vd.keys():
            out.append(key)
        if len(out) > 1:
            out.pop(0)
        return out

    def loadText(self):
        self.text.delete('1.0', tk.END)
        vehicleName = self.selected.get()
        if vehicleName in self.vd:
            vehicle = self.vd.get(vehicleName)
            vid = vehicle.getViconID()
            sensors = vehicle.getSensors()
            self.text.insert(tk.END, "Name: "+vehicleName+"\n")
            self.text.insert(tk.END, "ViconID: "+str(vid))
            self.text.insert(tk.END, "\nSensor Info\n")
            self.text.insert(tk.END, "Name\t\tRefresh Rate\n")

            for sensor in sensors:
                sensorString = sensor.getName() + "\t\t" + str(sensor.getRate())
                self.text.insert(tk.END, sensorString)
