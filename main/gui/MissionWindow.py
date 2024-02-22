import tkinter as tk


class MissionWindow(tk.Toplevel):
    def __init__(self, *args, name, tasks, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=600, height=300)
        title = name + "- Mission Overview"
        self.title(title)
        self.tasks = tasks

        # screen elements
        self.bar = tk.Scrollbar(self)
        self.text = tk.Text(self, height=10, width=60)
        self.text.place(x=20, y=20)
        self.bar.place(x=510, y=20, height=200)
        self.bar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.bar.set)

        self.focus()
        self.grab_set()

        for s in self.loadTasks():
            self.text.insert(tk.END, s)

    def loadTasks(self):
        # This is wildly inefficient in terms of running time and could be simplified if we just give the vehicle object
        # An attribute for the vehicle name, would also save the vehicle dictionary shenanigans, but im too far in to
        # Want to change that at this moment

        out = ["Time\t Vehicle\t\t Topic\t\t Message\n"]

        for obj in self.tasks:
            task = obj.getTask()
            time = str(task.getTimeStamp())
            topic = str(task.getTopic())
            message = str(task.getMessage())
            vehicle = obj.getVehicle()
            vehicleName = vehicle.getName()
            string = time + "\t" + vehicleName + "\t\t" + topic + "\t\t" + message + "\n"
            out.append(string)

        return out