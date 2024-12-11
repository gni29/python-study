import os
os.chdir('/Users/pyoungjinji/python-study')
print(os.getcwd())
dir = os.popen('cd')
print(dir.read())
print(os.listdir())