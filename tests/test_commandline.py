import os
import subprocess

from asekuro.commandline import _testfile

class TestPathHandlingLocal:

    @classmethod
    def setup_class(cls):
        os.chdir("tests")

    @classmethod
    def teardown_class(cls):
        os.chdir("..")

    def test_tempfile_creation(self):
        assert _testfile("foobar.ipynb") == "foobar-test.ipynb"

    def test_good_nb(self):
        status = subprocess.call(['asekuro', 'test', 'good-nb.ipynb'])
        assert status == 0

    def test_data_nb(self):
        status = subprocess.call(['asekuro', 'test', 'data-nb.ipynb'])
        assert status == 0

    def test_bad_bn(self):
        status = subprocess.call(['asekuro', 'test', 'bad-nb.ipynb'])
        assert status == 2


class TestCommandLineOuter:

    def test_good_nb(self):
        status = subprocess.call(['asekuro', 'test', 'tests/good-nb.ipynb'])
        assert status == 0

    def test_data_nb(self):
        status = subprocess.call(['asekuro', 'test', 'tests/data-nb.ipynb'])
        assert status == 0

    def test_bad_bn(self):
        status = subprocess.call(['asekuro', 'test', 'tests/bad-nb.ipynb'])
        assert status == 2
