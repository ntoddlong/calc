#!/bin/env python3

#input_box = tk.Text()
#input_box.pack()
#output_box = tk.Text()
#output_box.pack()
#
#output_box.insert("0.0", input_box.get("1.0", tk.END))

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

def helloCallBack():
   print()

window = tk.Tk()

# dropdown frames
dropdown_frame = tk.Frame(master=window, bg="#4d4d4d")
dropdown_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
input_dropdown_frame = tk.Frame(master=dropdown_frame, bg="gray")
input_dropdown_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
go_frame = tk.Frame(master=dropdown_frame, bg="gray")
go_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
output_dropdown_frame = tk.Frame(master=dropdown_frame, bg="gray")
output_dropdown_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)


B = tk.Button(go_frame, text ="go", command = helloCallBack)

B.pack()

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
input_type_dropdown = tk.OptionMenu(input_dropdown_frame, input_type, *data_types)
input_type_dropdown.pack()

# output data_type dropdown
output_type_dropdown = tk.OptionMenu(output_dropdown_frame, output_type, *data_types)
output_type_dropdown.pack()

# input text box
input_box = tk.Text(master=input_frame)
input_box.pack()

# output text box
output_box = tk.Text(master=output_frame)
output_box.pack()


# font
def_font = tk_font.nametofont("TkDefaultFont")
def_font.config(size=16)

window.mainloop()

