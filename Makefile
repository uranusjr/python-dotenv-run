ALL: help

PYTHON = pipenv run python --

.PHONY: help build clean upload

help:
	@echo 'Available commands:'
	@echo '  help   - Display this message and exist'
	@echo '  build  - Rebuild package for PyPI publish (implies clean)'
	@echo '  clean  - Clean package artifects'
	@echo '  upload - Upload package to PyPI (implies build)'

build: clean
	$(PYTHON) setup.py sdist bdist_wheel

clean:
	rm -rf build dist docs/build *.egg-info
	find . -name \*.pyc -delete
	find . -name __pycache__ -exec rm -r {} +

upload: build
	pipenv run twine upload dist/*
