import os
import subprocess

from asekuro.common import _testfile
from asekuro.cli import clean, test
from click.testing import CliRunner


class TestPathHandlingLocal:

    @classmethod
    def setup_class(cls):
        os.chdir("tests/notebooks")

    @classmethod
    def teardown_class(cls):
        os.chdir("../..")

    def test_tempfile_creation(self):
        assert _testfile("foobar.ipynb") == "foobar-test.ipynb"

    def test_good_nb(self):
        status = subprocess.call(['asekuro', 'test', 'good-nb.ipynb'])
        assert status == 0

    def test_good_nb_meta(self):
        status = subprocess.call(['asekuro', 'test', 'good-nb-metadata.ipynb'])
        assert status == 0

    def test_data_nb(self):
        status = subprocess.call(['asekuro', 'test', 'data-nb.ipynb'])
        assert status == 0

    def test_bad_bn(self):
        status = subprocess.call(['asekuro', 'test', 'bad-nb.ipynb'])
        assert status == 2


class TestCommandLineWorksWithPath:

    def test_good_nb(self):
        status = subprocess.call(['asekuro', 'test', 'tests/notebooks/good-nb.ipynb'])
        assert status == 0

    def test_data_nb(self):
        status = subprocess.call(['asekuro', 'test', 'tests/notebooks/data-nb.ipynb'])
        assert status == 0

    def test_bad_bn(self):
        status = subprocess.call(['asekuro', 'test', 'tests/notebooks/bad-nb.ipynb'])
        assert status == 2

    def test_good_nb_meta(self):
        status = subprocess.call(['asekuro', 'test', 'tests/notebooks/good-nb-metadata.ipynb'])
        assert status == 0

    def test_good_nb_autoreload(self):
        status = subprocess.call(['asekuro', 'test', 'tests/notebooks/nb-autoreload.ipynb'])
        assert status == 0


class TestKloptCommands:

    def test_good_nb(self):
        status = subprocess.call(['asekuro', 'check', 'tests/functions.ipynb', 'tests/functions-solution.py'])
        assert status == 0

    def test_clean_good_nb(self):
        status = subprocess.call(['asekuro', 'check', 'tests/functions.ipynb', 'tests/functions-solution-fail.py'])
        assert status == 2


class TestCommandsWorkWithWildCards:

    def test_clean_wildcard(self):
        runner = CliRunner()
        result = runner.invoke(clean, input='tests/notebooks/*.ipynb')
        assert not result.exception

    def test_multi_file(self):
        runner = CliRunner()
        result = runner.invoke(clean, input='tests/notebooks/data-nb.ipynb tests/notebooks/good-nb.ipynb')
        assert not result.exception

    def test_test_wildcard(self):
        runner = CliRunner()
        result = runner.invoke(test, input='tests/notebooks/good*.ipynb')
        assert not result.exception

    def test_test_multi_file(self):
        runner = CliRunner()
        result = runner.invoke(test, input='tests/notebooks/good-nb.ipynb tests/notebooks/good-nb-metadata.ipynb')
        assert not result.exception
