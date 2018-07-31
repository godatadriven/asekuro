import subprocess


class TestCommandLine:

    def test_good_nb(self):
        status = subprocess.call(['asekuro', 'test', 'tests/good-nb.ipynb'])
        assert status == 0

    def test_bad_bn(self):
        status = subprocess.call(['asekuro', 'test', 'tests/bad-nb.ipynb'])
        assert status == 2


class TestDockerBuild:

    def test_docker_build_fails(self):
        status = subprocess.call(['docker', 'build', '-t', 'asekurodock', '.'])
        print(status)
        assert status == 2
