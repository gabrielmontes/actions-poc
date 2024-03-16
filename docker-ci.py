# Author: Gabriel Montes.
import docker
import argparse

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

def parser() -> dict:
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', type=str, required=True)
  parser.add_argument('--dockerfile', type=str,required=True)
  parser.add_argument('--tag', type=str, required=True)
  parser.add_argument('--repository', type=str, required=True)
  parser.add_argument('--username', type=str, required=True)
  parser.add_argument('--password', type=str, required=True, help=argparse.SUPPRESS)
  return parser.parse_args()

def main() -> None:
  args = parser()
  
  build(
    path = args.path,
    file = args.dockerfile,
    tag = args.repository + ":" + args.tag
  )

  login(username = args.username, password = args.password)
  
  for line in push(repository = args.repository, tag = args.tag):
    print(line)

if __name__ == '__main__':
  main()
