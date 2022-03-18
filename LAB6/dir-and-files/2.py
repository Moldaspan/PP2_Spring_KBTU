import os

WORKING_DIR = os.getcwd()

for item in os.listdir(WORKING_DIR):
    path = os.path.join(WORKING_DIR, item)
    print(path)
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))


