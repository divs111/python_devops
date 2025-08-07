from devops_commands import execute_commands

def docker_run():
    res = execute_commands("docker images")
    print(res)
docker_run()