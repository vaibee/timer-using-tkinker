import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=0, column=1)

        self.clock = tk.Label(self, text="00:00:00", font=("Courier", 20), width=10)
        self.clock.grid(row=1, column=1, stick="S")

        self.time_label = tk.Label(self, text="hour : min  : sec", font=("Courier", 10), width=17)
        self.time_label.grid(row=2, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=3, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=3, column=1, sticky="NW")

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=3, column=3, sticky="NE")

        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
        self.time = int(self.time_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

    def quit(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("SAI SVETHA")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
