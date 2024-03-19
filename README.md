# GitHub Action: Docker Build, Login, and Push

This GitHub Action automates the process of building a Docker image, logging in to a Docker registry, and pushing the image to the registry. It takes the following parameters:

- tag: The tag to be applied to the Docker image.
- repository: The name of the Docker repository where the image will be pushed.
- username: The username required to authenticate with the Docker registry.
- password: The password or access token used for authentication.

Usage:

To use this action in your GitHub workflow, you can include it as a step in your .github/workflows/docker-ci.yml file.

```bash
name: docker-ci-build
on: [push]

jobs:
  get-num-square:
    runs-on: ubuntu-latest
    name: Docker build and push to docker hub repository.
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: docker-ci-build
        id: docker-ci-build
        uses: ./
        with:
          tag: "test_action"
          repository: ${{ secrets.REPOSITORY }} 
          username: ${{ secrets.USERNAME }}
          token: ${{ secrets.TOKEN }}
```
