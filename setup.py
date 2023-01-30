import sys
import  cx_Freeze 
import os

from cx_Freeze.dist import build_exe
base = None

if sys.platform == "win32":
    base = "win32GUI"

os.environ["TCL_LIBRARY"] = r"C:\Users\rkabh\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\rkabh\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("vpad.py",base=base,icon="icon.ico")]
cx_Freeze.setup(
    name = "Notebook Text Editor",
    options={"build_exe":{"packages":["tkinter","os"],"include_files":["icon.ico","tcl86t.dll","tk86t.dll","icons2"]}},
    version="0.0001",
    description="Tkinter Application",
    executables = executables
)