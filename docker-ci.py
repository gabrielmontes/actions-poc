# Author: Gabriel Montes.
import docker

# client:
client = docker.from_env()

def docker_build(**args) -> None:
  return client.images.build(
    path = args["path"],
    dockerfile = args["file"],
    tag = args["tag"]
  )

def main() -> None:
  print(docker_build(
    path = ".",
    file = "Dockerfile",
    tag = "test"
  ))

if __name__ == '__main__':
  main()
