import  PyInstaller.__main__
import os
import sys

script_name   = 'pybomb.py'
compiled_name = 'PyBomb'

here_path     = os.path.abspath(os.path.dirname(__file__))
path_to_imgs  = os.path.join(here_path, 'imgs')
path_to_fonts = os.path.join(here_path, 'fonts')

icon = os.path.join(path_to_imgs, 'orangebomb.ico')

font_style = 'ScriptsoftRegular.ttf'

if 'win' in sys.platform.lower():
    os_separator = ';'
else:
    os_separator = ':'

PyInstaller.__main__.run([
    '--clean',
    '--log-level=DEBUG',
    '--onefile',
    '--windowed',
    f'--name={compiled_name}',
    f'-i={icon}',
    f'-p={here_path}',
    '--hidden-import=kivy',
    '--hidden-import=kivy_deps.sdl2',
    '--hidden-import=kivy_deps.glew',
    script_name
])