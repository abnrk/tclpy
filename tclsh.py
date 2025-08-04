import sys
import tkinter as tk
root = tk.Tcl()
root.eval(f"source {sys.argv[1]}")