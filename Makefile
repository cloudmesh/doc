all: html epub


epub:
	cd docs; make epub

html:
	cd docs; make html

watch:
	cd docs; make watch

view:
	open docs/build/html/index.html

eview:
	open docs/build/epub/cloudmesh.epub

