FROM jupyter/scipy-notebook

COPY . .
RUN python3 -m venv testvenv
RUN . testvenv/bin/activate
RUN pip install -r requirements.txt

# next we test the notebooks
RUN python asekuro/commandline.py test tests/bad-nb.ipynb