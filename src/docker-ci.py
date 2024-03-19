# Author: Gabriel Montes.
import docker
import os

# client:
client = docker.from_env()

def build(**args) -> tuple:
  return client.images.build(
    path = args["path"],
    dockerfile = args["file"],
    tag = args["tag"]
  )

def login(**args) -> str:
  return client.login(
    username = args["username"], 
    password = args["password"]
  )

def push(**args) -> str:
  return client.images.push(
    repository = args["repository"], 
    tag = args["tag"],
    stream = True,
    decode = True
  )

def find(name, path) -> str:
  for root, dirs, files in os.walk(path):
    if name in files:
      return os.path.join(root,name)

def get_env_variables() -> dict:
  env_variables: dict = {
    "tag": None, 
    "repository": None, 
    "username": None,
    "token": None
  }

  for var in env_variables:
    current_var = os.environ.get(var)
    if current_var:
      try:
        env_variables.update({var: current_var})
      except Exception:
        exit(f'ERROR: The environment {var} has not been provided.')

  return env_variables

def main() -> None:
  variables: dict = get_env_variables()
  working_dir = os.getcwd()
  dockerfile = find("Dockerfile", working_dir)

  build(
    path = working_dir,
    file = dockerfile,
    tag = f"{variables.get('repository')}:{variables.get('tag')}"
  )

  login(username = variables.get("username"), password = variables.get("token"))
  
  for line in push(repository = variables.get("repository"), tag = variables.get("tag")):
    print(line)

if __name__ == '__main__':
  main()
