import eel
from pathlib import Path
cwd = 'index.html'
# Set web files folder
dir = Path.cwd()
eel.init(dir)
# def say_hello_py(x):
#     print('Hello from %s' % x)

# say_hello_py('Python World!')
# eel.say_hello_js('Python World!')   # Call a Javascript function

#eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.

eel.start(str(cwd), mode='electron')
