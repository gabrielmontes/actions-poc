# GitHub Action: Docker Build, Login, and Push

This GitHub Action automates the process of building a Docker image, logging in to a Docker registry, and pushing the image to the registry. It takes the following parameters:

- tag: The tag to be applied to the Docker image.
- repository: The name of the Docker repository where the image will be pushed.
- username: The username required to authenticate with the Docker registry.
- password: The password or access token used for authentication.

Usage:

To use this action in your GitHub workflow, you can include it as a step in your .github/workflows/docker-ci.yml file.
