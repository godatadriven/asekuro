import fire
import nbformat
import subprocess
import logging
import sys
import os

stdout_handler = logging.StreamHandler(sys.stdout)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(levelname)s - %(message)s',
    handlers=[stdout_handler]
)
logger = logging.getLogger('asekuro')


def _cwd(nbpath):
    """
    Changes the current working directory, relative to jupyter notebook path.
    We want to emulate the %load as if we're in the notebook itself. Hence this func.
    We also return the folder and filename of the path.
    :param nbpath: Path to the notebook that needs to be tested.
    """
    logger.debug(f"directory of script calling {os.getcwd()}")
    folder = os.path.dirname(nbpath)
    filename = os.path.basename(nbpath)
    if folder == "":
        folder = os.getcwd()
    os.chdir(folder)
    logger.debug(f"directory for rest of script {os.getcwd()}")
    return folder, filename


def _cells(nb):
    """
    Returns a generator with reference to cells in the passed notebook.
    :param nb: Jupyter Notebook Object
    :return: generator with cell references
    """
    if nb.nbformat < 4:
        for ws in nb.worksheets:
            for cell in ws.cells:
                yield cell
    else:
        for cell in nb.cells:
            yield cell


def _strip_output(nb):
    """
    Give it a notebook and it will change all output cells to become empty.
    :param nb: Jupyter Notebook Object
    :return: Jupyter Notebook Object
    """
    nb.metadata.pop('signature', None)
    for cell in _cells(nb):
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'prompt_number' in cell:
            cell['prompt_number'] = None
    return nb


def _testfile(nbpath):
    """
    Creates a path where to place a testing notebook.
    New file with have `-test.ipynb` at the end and is placed in same dir.
    :param nbpath: Path to the notebook that needs to be tested.
    """
    return nbpath.replace(".ipynb", "-test.ipynb")


def clean_notebook(nbpath):
    """
    Takes a notebook file on disk and removes all cell output.
    :param nbpath: Path to the notebook that needs to be cleaned of output.
    """
    logger.debug(f"about to strip {nbpath} of output")
    with open(nbpath, 'r') as f:
        notebook = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    notebook = _strip_output(notebook)
    with open(nbpath, 'w', encoding='utf8') as f:
        nbformat.write(notebook, f)
    logger.debug(f"{nbpath} is now stripped")


def make_testable_notebook(nbpath):
    """
    Creates a new notebook that is ready for testing. New file with have `-test.ipynb` at the end.
    :param nbpath: Path to the notebook that needs to be tested.
    """
    logger.debug(f"about to prepare {nbpath} for testing")
    with open(nbpath, 'r') as f:
        notebook = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    for cell in _cells(notebook):
        if cell['cell_type'] == 'code':
            if '%load' in cell['source']:
                logger.debug(f'found %load-magic in cell with id={cell["execution_count"]}')
                logger.debug(cell['source'])
                py_path = cell['source'].replace('%load ', '')
                with open(py_path, 'r') as f:
                    cell['source'] = f.read()
    nbformat.write(notebook, open(_testfile(nbpath=nbpath), mode='w'))
    logger.debug(f"wrote notebook ready for testing over at {_testfile(nbpath=nbpath)}")


def test_notebook(nbpath):
    """
    Takes a path to a notebook and then:
    - prepares it for testing by making a new notebook that is testable [because %load]
    - test said temporary file with `pytest --nbval-lax`
    - remove said temporary test file
    :param nbpath: Path to the notebook that needs to be tested.
    """
    logger.debug(f"about to test {nbpath}")
    folder, filename = _cwd(nbpath)
    make_testable_notebook(nbpath=filename)
    clean_notebook(nbpath=_testfile(filename))
    status = subprocess.call(['pytest', '--nbval-lax', '--verbose', _testfile(nbpath=filename)])
    logger.debug(f"removing temporary testing notebook {_testfile(nbpath=filename)}")
    os.remove(_testfile(nbpath=filename))
    logger.debug(f"testing done for {nbpath}")
    if status == 1:
        logger.debug(f"error was found so exiting with error code 1")
        sys.exit(2)


def main():
    fire.Fire({
        'test': test_notebook,
        'clean': clean_notebook
    })


if __name__ == "__main__":
    main()