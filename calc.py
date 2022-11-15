#!/bin/env python3

import tkinter as tk
import tkinter.font as tk_font

data_types = [
        "binary",
        "hex",
        "decimal",
        "ascii",
        ]

data_sizes = [
        "bytes",
        "kilobytes",
        "megabytes",
        "gigabytes",
        "terrabytes",
        "petabytes",
        "zettabytes",
        "yottabytes",
        ]

def handle_keypress(event):
    go_callback()

def go_callback():
    output_box.delete("0.0", tk.END)
    output_box.insert("0.0", convert(input_box.get("0.0", tk.END)))

def convert(inp) -> str:
    match input_type.get():
        case "binary":
            print("input is binary")
        case "hex":
            print("input is hex")
        case "decimal":
            print("input is decimal")
        case "ascii":
            print("input is ascii")
        case _:
            print("input is ",input_type.get())
    match output_type.get():
        case "binary":
            print("output is binary")
        case "hex":
            print("output is hex")
        case "decimal":
            print("output is decimal")
        case "ascii":
            print("output is ascii")
        case _:
            print("output is ",output_type.get())
    return inp

def input_dropdown_callback(selection):
    pass 
def output_dropdown_callback(selection):
    pass

window = tk.Tk()

# bind keypress event to handle_keypress()
window.bind("<Control-Return>", handle_keypress)

# font
def_font = tk_font.nametofont("TkDefaultFont")
def_font.config(size=16)

# dropdown frames
dropdown_frame = tk.Frame(master=window, bg="#4d4d4d")
dropdown_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
input_dropdown_frame = tk.Frame(master=dropdown_frame, bg="gray")
input_dropdown_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
go_frame = tk.Frame(master=dropdown_frame, bg="gray")
go_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
output_dropdown_frame = tk.Frame(master=dropdown_frame, bg="gray")
output_dropdown_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

# go button
go_button = tk.Button(go_frame, text ="go", command = go_callback)
go_button.pack()

# input frames
input_frame = tk.Frame(master=window, bg="gray")
input_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
output_frame = tk.Frame(master=window, bg="gray")
output_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# data_type dropdown defaults
input_type = tk.StringVar(input_frame)
input_type.set(data_types[2])
output_type = tk.StringVar(output_frame)
output_type.set(data_types[0])

# input data_type dropdown
input_type_dropdown = tk.OptionMenu(input_dropdown_frame, input_type, *data_types, command=input_dropdown_callback)
input_type_dropdown.pack()

# output data_type dropdown
output_type_dropdown = tk.OptionMenu(output_dropdown_frame, output_type, *data_types, command=output_dropdown_callback)
output_type_dropdown.pack()

# input text box
input_box = tk.Text(master=input_frame)
input_box.pack()

# output text box
output_box = tk.Text(master=output_frame)
output_box.pack()

window.mainloop()
