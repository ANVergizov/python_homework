import os


maindir = 'my_project'
dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

os.mkdir(maindir)
os.chdir(maindir)
for i in dirs:
    os.makedirs(i)

