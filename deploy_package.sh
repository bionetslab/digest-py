# build dist
python setup.py sdist

# test on test pypi
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/biodigest-0.1.0.tar.gz

# upload to pypi
python3 -m twine upload dist/biodigest-0.1.0.tar.gz