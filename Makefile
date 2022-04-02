all: html epub


epub:
	cd documentation; make epub

html:
#	sphinx-autogen documentation/source/index.rst
#	cd documentation/source/; sphinx-apidoc cloudmesh-common. -o junk
	cd documentation; make html

view:
	open documentation/build/html/index.html

eview:
	open documentation/build/epub/cloudmesh.epub
