import os
from commands import run_command, save_requirements_no_versions
from git_utils import initialize_git

def create_env_example_file(use_postgres):
    with open(".env_example", "w") as env_file:
        env_file.write(f"EXTERNAL_PORT=\n")
        if use_postgres:
            env_file.write(
                f"POSTGRES_DB=\nPOSTGRES_USER=\nPOSTGRES_PASSWORD=\nPOSTGRES_PORT=\n"
            )

def create_env_files(project_name, external_port, use_postgres, postgres_config=None):
    with open(".env", "w") as env_file:
        env_file.write(f"EXTERNAL_PORT={external_port}\n")
        if use_postgres:
            env_file.write(
                f"POSTGRES_DB={postgres_config['db']}\n"
                f"POSTGRES_USER={postgres_config['user']}\n"
                f"POSTGRES_PASSWORD={postgres_config['password']}\n"
                f"POSTGRES_PORT={postgres_config['port']}\n"
            )
    create_env_example_file(use_postgres)
            

def create_docker_compose(project_name, external_port, use_postgres, project_type, postgres_config=None):
    with open("docker-compose.yml", "w") as f:
        f.write(f"""version: '3'
services:
  web:
    build: .
""")
        if project_type == "django":
            f.write(f"""
    command: python manage.py runserver 0.0.0.0:$EXTERNAL_PORT
""")
        else:
            f.write(f"""
    command: python app.py --host 0.0.0.0 --port $EXTERNAL_PORT
""")
        f.write(f"""
    ports:
      - "$EXTERNAL_PORT:$EXTERNAL_PORT"
    env_file:
      - .env
""")
        if use_postgres:
            f.write(f"""
  db:
    image: postgres:13
    ports:
      - "${{POSTGRES_PORT}}:5432"
    environment:
      POSTGRES_DB: $POSTGRES_DB
      POSTGRES_USER: $POSTGRES_USER
      POSTGRES_PASSWORD: $POSTGRES_PASSWORD
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app_network

networks:
  app_network:
volumes:
  postgres_data:
""")

def create_dockerfile(project_type, project_name, external_port):
    with open("Dockerfile", "w") as f:
        f.write(f"""# Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
""")

def setup_project(project_name, project_type, github_username, github_repo_name, external_port, use_postgres, postgres_config=None):
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    run_command("python3 -m venv venv")
    run_command("source venv/bin/activate")

    if project_type == "django":
        run_command("pip install django psycopg2-binary")
        run_command(f"django-admin startproject {project_name} .")
    elif project_type == "flask":
        run_command("pip install flask psycopg2-binary")
        with open("app.py", "w") as f:
            f.write("""from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({'message': 'Hello, Flask!'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
""")
    
    save_requirements_no_versions()
    run_command("rm -rf venv")
    create_env_files(project_name, external_port, use_postgres, postgres_config)
    create_dockerfile(project_type, project_name, external_port)
    create_docker_compose(project_name, external_port, use_postgres, project_type, postgres_config)
    initialize_git(project_name, github_username, github_repo_name)
