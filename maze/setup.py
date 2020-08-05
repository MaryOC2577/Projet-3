"""Installation file for maze."""

from cx_Freeze import setup, Executable

setup(
    name="maze",
    version="1.0",
    description="Get out of the maze.",
    executables=[Executable("__main__.py")],
)
