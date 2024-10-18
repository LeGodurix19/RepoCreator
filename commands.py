import subprocess

class CommandError(Exception):
    pass

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        raise CommandError(result.stderr)
    return result.stdout

def save_requirements_no_versions():
    result = run_command("pip freeze")
    # Filtre les packages qui contiennent un chemin absolu
    packages = [line.split('==')[0] for line in result.splitlines() if "@" not in line]
    with open("requirements.txt", "w") as f:
        f.write("\n".join(packages))
