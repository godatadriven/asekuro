import subprocess


class TestDockerBuild:

    def test_docker_build_fails(self):
        status = subprocess.call(['docker', 'build', '-t', 'asekurodock', '.'])
        assert status == 2
