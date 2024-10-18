from commands import run_command

def initialize_git(project_name, github_username, github_repo_name):
    run_command("git init")
    with open(".gitignore", "w") as gitignore:
        gitignore.write("venv/\n.env\n")
    run_command("git add .")
    run_command("git commit -m 'Initial commit'")
    run_command(f"git remote add origin https://github.com/{github_username}/{github_repo_name}.git")
    run_command("git branch -M main")

def push_to_github(github_username, github_repo_name):
    try:
        run_command("git push -u origin main")
        print("Successfully pushed to GitHub repository!")
    except Exception as e:
        print(f"[Error] Failed to push to GitHub: {e}")
