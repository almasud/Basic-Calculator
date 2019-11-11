import tkinter as tk
import tkinter.messagebox

expression = ""
root = tk.Tk()
input_text = tk.StringVar()

# Creating basic window
root.geometry("325x355")  # width 325 and height 355
root.resizable(0, 0)
root.title("Calculator")
root.iconbitmap(r"calculator.ico")

# Update the input field whenever enter a number
def btn_press(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Clear the last input
def btn_clear_last():
    global expression
    expression = expression[:len(expression) - 1]
    input_text.set(expression)

# Clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Calculate the expression present in input field
def btn_equal():
    global expression
    
    try:
        result = str(eval(expression))
        input_text.set(result)
    except:
        input_text.set("Error")
        expression = ""

# Creating a Frame for the input field
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=5, pady=5)

# Creating a input field inside the 'Frame'
input_field = tk.Entry(input_frame, font=('arial', 16, 'bold'), 
    textvariable=input_text, bd=2)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10, fill=tk.X)

# Creating another Frame for the button bellow of the 'input_frame'
btns_frame = tk.Frame(root, bg="grey")
btns_frame.pack(padx=5)

# First row
clear_btn = tk.Button(btns_frame, text="C", fg="black", width=21, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=btn_clear)
clear_btn.grid(row=0, columnspan=2)
divide_btn = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=lambda: btn_press("/"))
divide_btn.grid(row=0, column=2)
clear_last_btn = tk.Button(btns_frame, text="<-", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=btn_clear_last)
clear_last_btn.grid(row=0, column=3)

# Second row
seven_btn = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("7"))
seven_btn.grid(row=1, column=0)
eight_btn = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("8"))
eight_btn.grid(row=1, column=1)
nine_btn = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("9"))
nine_btn.grid(row=1, column=2)
multiply_btn = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=lambda: btn_press("*"))
multiply_btn.grid(row=1, column=3)

# Third row
four_btn = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("4"))
four_btn.grid(row=2, column=0)
five_btn = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("5"))
five_btn.grid(row=2, column=1)
six_btn = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("6"))
six_btn.grid(row=2, column=2)
minus_btn = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=lambda: btn_press("-"))
minus_btn.grid(row=2, column=3)

# Fourth row
one_btn = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("1"))
one_btn.grid(row=3, column=0)
two_btn = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("2"))
two_btn.grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("3"))
three.grid(row=3, column=2)
plus_btn = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=lambda: btn_press("+"))
plus_btn.grid(row=3, column=3)

# Fifth row
zero_btn = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=1, 
    bg="#fff", cursor="hand2", command=lambda: btn_press("0"))
zero_btn.grid(row=4, columnspan=2)
point_btn = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=lambda: btn_press("."))
point_btn.grid(row=4, column=2)
equal_btn = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=1, 
    bg="#eee", cursor="hand2", command=btn_equal)
equal_btn.grid(row=4, column=3)

# Create about menu
menu = tk.Menu(root)
root.config(menu=menu)
submenu = tk.Menu(menu)
menu.add_cascade(label="About", menu=submenu)
submenu.add_command(label="Developer", command=lambda: tkinter.messagebox
    .showinfo("Developer Info", "Name: Abdullah Almasud\nEmail: almasud.arm@gmail.com"))


if __name__ == "__main__":
    root.mainloop()
