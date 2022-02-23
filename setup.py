import sys # Imports are automatically detected (normally) in the script to freeze
import os 
import cx_Freeze
base = None 
from cx_Freeze import setup, Executable

if sys.platform=='win32':
    base = "Win32GUI"
#icon='icona.png'

#executables = [cx_Freeze.Executable("olg.py"),icon]    

target = Executable(
    script="olg.py",
    base="Win32GUI",
    #compress=False,
    #copyDependentFiles=True,
    #appendScriptToExe=True,
    #appendScriptToLibrary=False,
    icon="icona.ico"
)

cx_Freeze.setup(
        name = "Wordle",
        options = {"build_exe":{"packages":["tkinter","pandas","turtle","random"],"include_files":["words.txt","landing.png"]}},
        version="0.01",
        executables=[target]) 