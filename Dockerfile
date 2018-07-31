FROM jupyter/scipy-notebook

WORKDIR /tmp
RUN ls -lhat
COPY . .
RUN ls -lhat
RUN pwd

RUN pip install -r requirements.txt

# we test the notebooks. we really want this to break beause of the second notebook
RUN python asekuro/commandline.py test tests/data-nb.ipynb
RUN python asekuro/commandline.py test tests/bad-nb.ipynb
RUN python asekuro/commandline.py test tests/good-nb.ipynb