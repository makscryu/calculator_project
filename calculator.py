from customtkinter import *

GRAY = "#e0e0e0"
DARK_GRAY = "#c1c1c1"
BLUE = "#aaa6ff"
window = CTk()
window.geometry("400x600")
window.title("Calculator")

sum = ""
TEXT = ""

def update_entry():
    global sum
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, sum)
    entry.configure(state="disabled")

def equal():
    global sum
    try:
        result = str(eval(sum))
        sum = result
    except Exception:
        sum = "failed"
    update_entry()

def CE():
    global sum
    sum = ""
    update_entry()











entry = CTkEntry(window, placeholder_text=TEXT, state="disabled", font=CTkFont(size=14), width=400, height=100)
entry.place(x=0, y=0)

def divide():
    global sum, TEXT
    sum += " / "
    TEXT = sum
    update_entry()
button = CTkButton(window, text="/", command=divide, font=CTkFont(size=36, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=300, y=100)

button = CTkButton(window, text="failed", font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=200, y=100) 

button = CTkButton(window, text="CE", command=CE, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=100, y=100) 

button = CTkButton(window, text="failed", font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=0, y=100) 

def one():
    global sum, TEXT
    sum += "1"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="1", command=one, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=0, y=200) 
 
def two():
    global sum, TEXT
    sum += "2"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="2", command=two, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=100, y=200) 
 
def three():
    global sum, TEXT
    sum += "3"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="3", command=three, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=200, y=200) 

def multiply():
    global sum, TEXT
    sum += " * "
    TEXT = sum
    update_entry()
button = CTkButton(window, text="*", command=multiply, font=CTkFont(size=48, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=300, y=200) 

def four():
    global sum, TEXT
    sum += "4"
    TEXT = sum
    update_entry() 
button = CTkButton(window, text="4", command=four, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=0, y=300) 

def five():
    global sum, TEXT
    sum += "5"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="5", command=five, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=100, y=300) 

def six():
    global sum, TEXT
    sum += "6"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="6", command=six, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=200, y=300) 

def minus():
    global sum, TEXT
    sum += " - "
    TEXT = sum
    update_entry()
button = CTkButton(window, text="-", command=minus, font=CTkFont(size=48, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=300, y=300) 

def seven():
    global sum, TEXT
    sum += "7"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="7", command=seven, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=0, y=400) 

def eight():
    global sum, TEXT
    sum += "8"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="8", command=eight, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=100, y=400) 

def nine():
    global sum, TEXT
    sum += "9"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="9", command=nine, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=GRAY)
button.place(x=200, y=400) 

def plus():
    global sum, TEXT
    sum += " + "
    TEXT = sum
    update_entry()
button = CTkButton(window, text="+", command=plus, font=CTkFont(size=36, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=300, y=400) 

def negate_positate():
    global sum, TEXT
    if sum and sum[0] == "-":
        sum = sum[0] = ""
    else:
        sum = "-" + sum
    TEXT = sum
    update_entry()
button = CTkButton(window, text="+/-", command=negate_positate, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=0, y=500)

def zero():
    global sum, TEXT
    sum += "0"
    TEXT = sum
    update_entry()
button = CTkButton(window, text="0", command=zero, font=CTkFont(size=24, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=100, y=500)

def dot():
    global sum, TEXT
    sum += "."
    TEXT = sum
    update_entry()
button = CTkButton(window, text=".", command=dot, font=CTkFont(size=50, weight="bold"), width=100 ,height=100, text_color="black", fg_color=DARK_GRAY)
button.place(x=200, y=500)

button = CTkButton(window, text="=", command=equal, font=CTkFont(size=48, weight="bold"), width=100 ,height=100, text_color="black", fg_color=BLUE)
button.place(x=300, y=500)

window.mainloop()
