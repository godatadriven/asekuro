FROM jupyter/scipy-notebook

USER root
COPY . .

RUN python setup.py install

# we test the notebooks.
RUN asekuro test tests/data-nb.ipynb
# we really want this to break beause of the second notebook
RUN asekuro test tests/bad-nb.ipynb
# we shouldn't see it come here
RUN asekuro test tests/good-nb.ipynb