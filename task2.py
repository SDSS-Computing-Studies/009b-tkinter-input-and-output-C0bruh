"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *

win = tk.Tk()

eoutput = StringVar()
eoutput.set("Answer")

sign1 = StringVar()
sign1.set("-")
sign2 = StringVar()
sign2.set("+")

def trinomial():
    a = 1
    b = int(e1.get())
    c = int(e2.get())

    a1 = (-b + (b**2-4*a*c) ** (1/2)) / (2)
    a2 = (-b - (b**2-4*a*c) ** (1/2)) / (2)

    o1 = -1*a1
    o2 = -1*a2

    x = str(o1)
    y = str(o2)