import os
from glob import glob
from cloudmesh.common.util import banner
# os.system("sphinx-autogen documentation/source/index.rst")
from cloudmesh.common.util import writefile

banner("install cloudmesh")
os.system("pip install cloudmesh-installer")
os.system("mkdir -p github")
os.system("cd github; cloudmesh-installer get"
          "cms gpu pi-burn pi-cluster ssh mpi markdown installer diagram catalog")
modules = glob("github/cloudmesh-*")
os.system("mkdir -p documentation/source/cloudmesh")
# merge
package_list = []
for module in modules:

    name = module.replace("github/cloudmesh-", "")
    print (module, name)
    command = f"cp -r {module}/cloudmesh documentation/source/cloudmesh"
    print (command)
    os.system(command)
    package_list.append(f"modules/{name}")

os.system(f"sphinx-apidoc documentation/source/cloudmesh -o documentation/source/modules -f")


page = """
Packages
==============

.. toctree::
   :maxdepth: 4

""" + "   " + "\n   ".join(package_list)

print (page)

writefile("documentation/source/list.rst", page)

os.system("make html")

