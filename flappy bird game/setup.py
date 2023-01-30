import sys
import  cx_Freeze 
import os

from cx_Freeze.dist import build_exe
base = None

if sys.platform == "win32":
    base = "win32GUI"

os.environ["TCL_LIBRARY"] = r"C:\Users\rkabh\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\rkabh\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py",base=base,icon="bird.png")]
cx_Freeze.setup(
    name = "Flappy Bird Game",
    options={"build_exe":{"packages":["pygame","os"],"include_files":["bird.png","tcl86t.dll","tk86t.dll","gallery","gallery/sprites","gallery/audio"]}},
    version="0.0001",
    description="py game",
    executables = executables
)