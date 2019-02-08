import subprocess


class TestDockerBuild:

    def test_docker_build_fails(self):
        status = subprocess.call(['docker', 'build', '-t', 'asekurodock', '-f', 'tests/Dockerfile.test1', '.'])
        assert status == 2

    def test_docker_build_is_fine(self):
        status = subprocess.call(['docker', 'build', '-t', 'asekurodock', '-f', 'tests/Dockerfile.test2', '.'])
        assert status == 0
