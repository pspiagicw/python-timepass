test:
	python -m unittest discover
	rm -rf Example_Project
build:  test
	python setup.py sdist bdist_wheel
clean: 
	rm -rf build dist Project_Builder.egg-info
install: build 
	pip install dist/Project_Builder-0.1-py3-none-any.whl
	make clean
uninstall:
	pip uninstall project_builder
lint: clean
	yapf -r -i project_builder
