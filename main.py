from time import sleep
from tkinter import(
    Tk,
    Label,
    Button
)



class Clock(Tk):
    TARGET = 600
    timer = 0
    def __init__(self) -> None:
        super().__init__()
        self.title("Աchqer timer v. 0.0.1")
        self.geometry("250x100")

        label = Label(self, text="1", font=("Arial", 30))
        label.place(x=30, y=30)

        restart_btn = Button(self, text="restart", command=lambda lbl=label: self.restart(lbl))
        restart_btn.place(x=190, y=40)

        self.show_time(label=label)

        self.mainloop()

    def eyes(self, label: Label):
        self["bg"] = "purple"
        label["bg"] = "purple"
        label["fg"] = "yellow"

    def restart(self, label: Label):
        Clock.timer = 0
        self.show_time(label)
    
    def show_time(self, label: Label):
        Clock.timer += 1
        label["text"] = f"{Clock.timer}/600"
        timer_id = label.after(1000, lambda a=label: self.show_time(a))
        if Clock.timer == Clock.TARGET:
            label.after_cancel(timer_id)
            self.eyes(label)



 




Clock()



