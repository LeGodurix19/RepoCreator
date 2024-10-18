from validators import (
    get_valid_project_name, 
    get_valid_project_type,
    get_valid_github_username,
    get_valid_github_repo_name,
    get_valid_external_port,
    get_use_postgres,
    get_postgres_config
)
from setup import setup_project
from git_utils import push_to_github

def main():
    print("Welcome to the Project Setup Script!")
    project_name = get_valid_project_name()
    project_type = get_valid_project_type()
    github_username = get_valid_github_username()
    github_repo_name = get_valid_github_repo_name()
    external_port = get_valid_external_port()
    use_postgres = get_use_postgres()
    postgres_config = get_postgres_config() if use_postgres else None

    try:
        setup_project(
            project_name=project_name,
            project_type=project_type,
            github_username=github_username,
            github_repo_name=github_repo_name,
            external_port=external_port,
            use_postgres=use_postgres,
            postgres_config=postgres_config
        )
        push_to_github(github_username, github_repo_name)
        print("Project setup successfully completed and pushed to GitHub!")
    except Exception as e:
        print(f"[Error] Project setup failed: {e}")

if __name__ == "__main__":
    main()
