import tkinter as tk


class SensorWindow(tk.Toplevel):
    def __init__(self, *args, name, sensors, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=600, height=300)
        title = name + "- Sensors"
        self.title(title)
        self.sensors = sensors

        # screen elements
        self.bar = tk.Scrollbar(self)
        self.text = tk.Text(self, height=10, width=60)
        self.text.place(x=20, y=20)
        self.bar.place(x=510, y=20, height=200)
        self.bar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.bar.set)

        self.focus()
        self.grab_set()

        for s in self.loadSensors():
            self.text.insert(tk.END, s)

    def loadSensors(self):
        out = ["Location\t\t Name\t\t Refresh Rate\n"]
        for row in self.sensors:
            sensor = row[1]
            location = row[0]
            out.append(location + "\t\t" + sensor.getName() + "\t\t" + str(sensor.getRate()) + "\n")

        return out
