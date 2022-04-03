import os
from shutil import copy
here=os.getcwd()
os.mkdir( "Fareeda")
os.chdir(os.path.join(here,"Fareeda"))
for i in range(6):
    file=f"{i}.txt"
    with open(file,'w')as f:
        f.write(f"This is file {i}")
os.mkdir(f"{here}\os_project")
for filename in os.listdir():
    copy(filename,os.path.join(here, "os_project"))