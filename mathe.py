import numpy as np
from tkinter import *

app = Tk()
app.title("MathSolver")
header = Label(app, text="Freetime", font=("calibri", 14), bg="grey", )


header.grid()
app.mainloop()


a = [-4, -6, 4]
b = [-1, -2, 3]

print("Skalarprodukt:", np.dot(a,b))
print("Crossproduct: ",np.cross(a, b))