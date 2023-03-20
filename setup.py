from cx_Freeze import setup, Executable

executables = [Executable("atalho.py", base=None, icon="image/icone.ico")]

build_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(
    name="NomeDoSeuApp",
    version="0.1",
    description="Descrição do Seu App",
    options={"build_exe": build_options},
    executables=executables
)
