from tkinter import *
from tkinter import messagebox

# configuration to window size, color and title
root = Tk()
root.title("Ticket Sales")
root.geometry("500x600")
root.config(bg="#212529")


# blueprint
class clsTicketSales:
    def __init__(self, window):
        self.cellnumber = Label(window, text="Enter Cell Number:")
        self.cellnumber.config(bg="#212529", fg="white")
        self.cellnumber.place(relx="0.1", rely="0.4")
        self.cellnumber_entry = Entry(window)
        self.cellnumber_entry.place(relx="0.5", rely="0.4")
        self.tprice = Label(window, text="Select Ticket Category:")
        self.tprice.config(bg="#212529", fg="white")
        self.tprice.place(relx="0.1", rely="0.5")
        self.options = ["Movies", "Soccer", "Theater"]
        self.option = StringVar()
        self.option.set('Select...')
        self.optionsbox = OptionMenu(window, self.option, *self.options)
        self.optionsbox.place(relx="0.5", rely="0.5")
        self.nr_tickets = Label(window, text="Number of Tickets Bought")
        self.nr_tickets.config(bg="#212529", fg="white")
        self.nr_tickets.place(relx="0.1", rely="0.6")
        self.nr_tickets_entry = Spinbox(window, from_=0, to=50, width="5")
        self.nr_tickets_entry.place(relx="0.5", rely="0.6")
        self.calculate = Button(window, text="Calculate Ticket", width="12", command=self.calculate)
        self.calculate.place(relx="0.1", rely="0.7")
        self.clearbtn = Button(window, text="Clear", width="12", command=self.clear)
        self.clearbtn.place(relx="0.5", rely="0.7")
        self.frame = Frame(window, width=400, height=100, relief="groove", borderwidth=2)
        self.frame.place(relx="0.1", rely="0.8")
        self.answer = Label(self.frame, text=" ")
        self.answer.place(relx="0.3", rely="0.3")

    # Calculate function created
    def calculate(self):

        numbertickets = int(self.nr_tickets_entry.get())
        vat = 0.14

        # try used to show any errors
        try:
            if len(self.cellnumber_entry.get()) > 10 or len(self.cellnumber_entry.get()) < 10:
                raise ValueError
            elif self.option.get() == "Select...":
                raise ValueError
            elif self.option.get() == "Movies":
                result = 75 * int(self.nr_tickets_entry.get())
                final = result + result * vat
                self.answer.config(text=final)
            elif self.option.get() == "Soccer":
                result = 40 * int(self.nr_tickets_entry.get())
                final = result + result * vat
                self.answer.config(text=final)
            elif self.option.get() == "Theater":
                result = 100 * int(self.nr_tickets_entry.get())
                final = result + result * vat
                self.answer.config(text=final)

        # error shown here
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter information accordingly")

    # function for clear button created
    def clear(self):
        self.cellnumber_entry.delete(0, END)
        self.nr_tickets_entry.delete(0, END)
        self.option.set("Select...")


clsTicketSales(root)
root.mainloop()
