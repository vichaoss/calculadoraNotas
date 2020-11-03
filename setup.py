from cx_Freeze import setup, Executable

base = None

executables = [Executable("desktopApp.py", base=base)]

packages = ["tkinter"]
build_exe_options = {"packages": packages}

options = {
    'build_exe': build_exe_options
}

setup(
    name="Calculadora de Notas",
    options=options,
    version="2.0",
    description='Nopp',
    executables=executables
)
