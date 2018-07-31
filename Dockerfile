FROM jupyter/scipy-notebook

USER root
COPY . .
RUN chmod 777 -R .
RUN pip install -r requirements.txt

# we test the notebooks.
RUN python asekuro/commandline.py test tests/data-nb.ipynb
# we really want this to break beause of the second notebook
RUN python asekuro/commandline.py test tests/bad-nb.ipynb
# we shouldn't see it come here
RUN python asekuro/commandline.py test tests/good-nb.ipynb