import numpy as np
from tkinter import *

def string_to_vector(v1, v2):
    v1_c = v1.split(",")
    v1 = [int(x) for x in v1_c]
    v2_c = v2.split(",")
    v2 = [int(x) for x in v2_c]
    return v1, v2

def crossproduct():
    v1, v2 = string_to_vector(v1_variable.get(), v2_variable.get())
    result.config(text=np.cross(v1, v2))

def scalarproduct():
    v1, v2 = string_to_vector(v1_variable.get(), v2_variable.get())
    result.config(text=np.dot(v1, v2))

def vectors():
    global v1_variable, v2_variable, result
    v_screen = Toplevel(app)
    header = Label(v_screen, text="Vectors", font=("calibri", 30), bg="grey")

    v1_variable = StringVar()
    v2_variable = StringVar()
    
    v1_label = Label(v_screen, text="Vector 1:")
    v1_entry = Entry(v_screen, textvariable=v1_variable)
    v2_label = Label(v_screen, text="Vector 2:")
    v2_entry = Entry(v_screen, textvariable=v2_variable)

    cross_product_button = Button(v_screen, text="Crossproduct", command=crossproduct)
    scalar_product_button = Button(v_screen, text="Scalarproduct", command=scalarproduct)

    result = Label(v_screen, text="...")


    # .grid on the Toplevel window
    header.grid(row=0, columnspan=2)
    v1_label.grid(row=1, column=0)
    v2_label.grid(row=1, column=1)
    v1_entry.grid(row=2, column=0)
    v2_entry.grid(row=2, column=1)
    cross_product_button.grid(row=3, column=0)
    scalar_product_button.grid(row=3, column=1)
    result.grid(row=4)



def angels():
    a_screen = Toplevel(app)

def start():
    if ag_dd_value.get() == "Vectors":
        vectors()
    if ag_dd_value.get() == "Angels":
        angels()

app = Tk()
app.title("MathSolver")
header = Label(app, text="Freetime", font=("calibri", 30), bg="grey", )

container_options = LabelFrame(app, text="Choose a tool:")

ag_dd_value = StringVar()
sub_heading_analytic_geometry = Label(container_options, text="Analytical Geometry")
ag_dropdown = OptionMenu(container_options, ag_dd_value, "Vectors", "Angels")
ag_button = Button(container_options, text="Start tool", command=start)

# put elements on app window
header.grid(row=0, columnspan=3)
container_options.grid(row=1, columnspan=3)
sub_heading_analytic_geometry.grid(row=0, column=0)
ag_dropdown.grid(row=1, column=0)
ag_button.grid(row=2, column=0)
app.mainloop()



# a = [-4, -6, 4]
# b = [-1, -2, 3]

# print("Skalarprodukt:", np.dot(a,b))
# print("Crossproduct: ", np.cross(a, b))