import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x150")

def show_input():
    user_input = entry.get()
    print("User input:", user_input)
    output_label.config(text="User input:" +user_input)


label = tk.Label(root, text="Enter something:")
label.pack(pady=10)


entry = tk.Entry(root, width=30)
entry.pack(pady=5)


button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)

output_label = tk.Label(root, text=" ")
output_label.pack(pady=10)



root.mainloop()

