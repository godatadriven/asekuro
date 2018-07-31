FROM jupyter/scipy-notebook

USER root
COPY . .

RUN python setup.py install

# we really want this to break beause of this notebook
RUN asekuro test tests/bad-nb.ipynb

# we shouldn't see it come here
RUN asekuro test tests/data-nb.ipynb
RUN asekuro test tests/good-nb.ipynb