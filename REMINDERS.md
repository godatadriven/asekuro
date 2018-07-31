### Local development

Python can help you. Don't reinstall all the time, rather use a virtulenv that has a link to the code.

```
python setup.py develop
```

### Pushing New Version to PyPi

From the root folder, run:

```
rm -rf dist
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*
```