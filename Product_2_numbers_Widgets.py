from tkinter import *

window = Tk()
window.title("Taking the product of 2 numbers.")
window.geometry("400x200")

welcome_label = Label(text="Welcome, Please enter 2 numbers below:", fg="white", bg="blue")
number1 = Entry(window)
number2 = Entry(window)
output = Text(window, width=30, height=5)
def button_pressed():
  num1 = int(number1.get())
  num2 = int(number2.get())
  result = num1 * num2
  message = f"Your result is: {result}"
  output.insert(END, message)


button1 = Button(text="Submit", fg="white", bg="blue", command=button_pressed)

welcome_label.pack()
number1.pack()
number2.pack()
button1.pack()
output.pack()
window.mainloop()




