def get_valid_project_name():
    while True:
        project_name = input("Enter project name: ").strip()
        if project_name and all(c.isalnum() or c in '-_' for c in project_name):
            return project_name
        print("Invalid project name. Use only letters, numbers, hyphens, and underscores.")

def get_valid_project_type():
    while True:
        project_type = input("Enter project type (django or flask): ").strip().lower()
        if project_type in ['django', 'flask']:
            return project_type
        print("Invalid project type. Choose either 'django' or 'flask'.")

def get_valid_github_username():
    while True:
        github_username = input("Enter GitHub username: ").strip()
        if github_username and github_username.isalnum():
            return github_username
        print("Invalid GitHub username. Use only alphanumeric characters.")

def get_valid_github_repo_name():
    while True:
        github_repo_name = input("Enter GitHub repository name: ").strip()
        if github_repo_name and all(c.isalnum() or c in '-_' for c in github_repo_name):
            return github_repo_name
        print("Invalid GitHub repository name. Use only letters, numbers, hyphens, and underscores.")

def get_valid_external_port():
    while True:
        external_port = input("Enter external port (1024-65535): ").strip()
        if external_port.isdigit() and 1024 <= int(external_port) <= 65535:
            return external_port
        print("Invalid port number. Enter a number between 1024 and 65535.")

def get_use_postgres():
    while True:
        use_postgres = input("Use PostgreSQL? (yes or no): ").strip().lower()
        if use_postgres in ['yes', 'no']:
            return use_postgres == 'yes'
        print("Invalid choice. Enter 'yes' or 'no'.")

def get_postgres_config():
    config = {}
    config['db'] = input("Enter PostgreSQL database name: ").strip()
    config['user'] = input("Enter PostgreSQL user: ").strip()
    config['password'] = input("Enter PostgreSQL password: ").strip()
    config['port'] = input("Enter PostgreSQL port: ").strip()  # Port standard pour PostgreSQL
    return config
