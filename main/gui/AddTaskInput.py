import tkinter as tk


class AddTaskInput(tk.Toplevel):
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
        self.drop.place(x=150, y=150)

        self.label_drop = tk.Label(self, text="Vehicle:")
        self.label_drop.place(x=50, y=150)

        # set up features
        self.timeStampEntry = tk.Entry(self)
        self.timeStampEntry.place(x=150, y=20, width=130)

        self.label_timeStamp = tk.Label(self, text="Time stamp:")
        self.label_timeStamp.place(x=50, y=20)

        self.messageEntry = tk.Entry(self)
        self.messageEntry.place(x=150, y=60, width=130)

        self.label_message = tk.Label(self, text="ROS Message:")
        self.label_message.place(x=50, y=60)

        self.topicEntry = tk.Entry(self)
        self.topicEntry.place(x=150, y=100, width=130)

        self.label_topic = tk.Label(self, text="ROS Topic:")
        self.label_topic.place(x=50, y=100)

        self.doneButton = tk.Button(self, text="Done", command=self.done_pressed)
        self.doneButton.place(x=20, y=200, width=260)

        self.focus()
        self.grab_set()

    def done_pressed(self):
        # Use callback function to return to main window
        if self.selected.get() in self.vd:
            timeStamp = float(self.timeStampEntry.get())
            message = self.messageEntry.get()
            topic = self.topicEntry.get()
            vehicle = self.vd.get(self.selected.get())

            self.callback(timeStamp, message, topic, vehicle)

            # kill this window
            self.destroy()

    def loadOptions(self):
        out = ["Don't Select Me"]
        for key in self.vd.keys():
            out.append(key)
        if len(out) > 1:
            out.pop(0)
        return out