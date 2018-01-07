from cx_Freeze import setup,Executable
setup(
    name = "alarm_20_20_20",
    version = "0.1",
    description = "Utility",
    executables = [Executable("myalarm_20_20_20.py")])
