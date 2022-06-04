import os
import shutil

dir = 'my_project'

for root, dirs, files in os.walk(dir):
    for item in dirs:
        if item == 'templates':
            shutil.copytree(os.path.join(root, item),
                            os.path.join(dir, 'templates'),
                            dirs_exist_ok=True)
