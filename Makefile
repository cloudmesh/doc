all: html epub


epub:
	cd content; make epub

html:
	cd content; make html

watch:
	cd content; make watch

view:
	open content/build/html/index.html

eview:
	open content/build/epub/cloudmesh.epub

