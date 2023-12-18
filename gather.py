import os
from cloudmesh.common.util import writefile
import os

directory_path = '..'

all_directories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
cloudmesh_directories = [d for d in all_directories if d.startswith('cloudmesh-')]


toc = """
.. toctree::
    :maxdepth: 2

"""


for package in cloudmesh_directories:
    toc = toc + f"    {package}/index.rst\n"
    os.system(f"sphinx-apidoc -o docs/source/{package} ../{package}")

print (toc)

os.system("cd docs; make html")
os.system("open docs/build/html/index.html")