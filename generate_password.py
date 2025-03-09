from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import random, string, pyperclip

def copy(var):
	pyperclip.copy(var)

def generate_password(length):
	chars = string.ascii_letters
	all_chars =  string.ascii_letters + string.digits + string.punctuation
	chars_digits = string.ascii_letters + string.digits
	chars_punctuation = string.ascii_letters + string.punctuation
	
	if enabled1.get() == 1: # Generate latin letters, punctuation and digits
		passwords = "".join(random.choice(all_chars) for _ in range(length))
		copy(passwords)
		return passwords
	elif enabled2.get() == 1: #Generate latin letters and punctuation
		passwords = "".join(random.choice(chars_punctuation) for _ in range(length))
		copy(passwords)
		return passwords
	elif enabled3.get() == 1: # Generate latin letters and digits
		passwords = "".join(random.choice(chars_digits) for _ in range(length))
		copy(passwords)
		return passwords
	elif enabled4.get() == 1: # Generate latin letters
		passwords = "".join(random.choice(chars) for _ in range(length))
		copy(passwords)
		return passwords
	else:
		showinfo(title="Info", message="Select one action.")
		
		
def start():
	lengths = int(entry.get())
	result_text_password['text'] = generate_password(lengths)	

root = Tk()
root.geometry('350x250')
root.resizable(False, False)
root.title('Password Generate')

generate_button = ttk.Button(text="Generate Password", command=start)
generate_button.pack(fill=BOTH, side=BOTTOM)

enabled1 = IntVar()
enabled2 = IntVar()
enabled3 = IntVar()
enabled4 = IntVar()

result_text_password = ttk.Label(font=('Arial'))
result_text_password.pack()

entry = ttk.Entry()
entry.pack(expand=True)
entry.insert(0, '12')

check_button1 = ttk.Checkbutton(text="All latin letters, punctuation and digits.", variable=enabled1)
check_button2 = ttk.Checkbutton(text="All latin letters and punctuation.", variable=enabled2)
check_button3 = ttk.Checkbutton(text="All latin letters and digits.", variable=enabled3)
check_button4 = ttk.Checkbutton(text="Only latters", variable=enabled4)
check_button1.pack(padx=6, pady=6, anchor=NW)
check_button2.pack(padx=7, pady=7, anchor=NW)
check_button3.pack(padx=8, pady=8, anchor=NW)
check_button4.pack(padx=9, pady=9, anchor=NW)

root.mainloop()